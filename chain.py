import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import Qdrant
from qdrant_client import QdrantClient
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder,FewShotChatMessagePromptTemplate,PromptTemplate
from langchain.chains import create_sql_query_chain
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from operator import itemgetter
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
import streamlit as st
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
load_dotenv()

from prompts import final_prompt,answer_prompt


GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
LANGCHAIN_TRACING_V2=os.getenv("LANGCHAIN_TRACING_V2")
LANCHAIN_API_KEY=os.getenv("LANGCHAIN_API_KEY")

 

def gemini():
    return ChatGoogleGenerativeAI(model="gemini-1.5-pro")

def connect_db():
    db=SQLDatabase.from_uri("sqlite:///database.db")
    return db

def process_query(query):
    tmp=query.replace("```", "").strip()
    idx=tmp.find("SELECT")
    str=tmp[idx:]
    return str
 

@st.cache_resource 
def get_chain(qsn):
    llm = gemini()
    db = connect_db()
    generate_query = create_sql_query_chain(llm, db,final_prompt(qsn))
    execute_query = QuerySQLDataBaseTool(db=db)

    rephrase_answer = answer_prompt | llm | StrOutputParser()

    chain = (
        RunnablePassthrough.assign(query=generate_query)
        .assign(query=lambda d: {"query": process_query(d["query"])})
        .assign(result=itemgetter("query") | execute_query)
        | rephrase_answer
    )

    return chain

