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


from chain import get_chain



def create_history(messages):
    history=ChatMessageHistory()
    for message in messages:
        if message["role"]=="user":
            history.add_user_message(message["content"])
        else :
            history.add_ai_message(message["content"])
    return history



def run_chain(qsn,messages):
   
    chain=get_chain(qsn)
    history=create_history(messages)
    suf="""and in your first query response  give me just sql query i don't want title or other because this query directly exclued on database without any preprosesing that's way
        Instructions: 
        - Base your answer solely on the provided SQL Result. 
        - Do NOT include the SQL Query in your final response. 
        -If the question cannot be answered from the provided information or is unrelated, respond ONLY with: "I'm sorry. I can't answer your question."
        -formulate a natural language answer to the user question using the SQL result.
    """
    response = chain.invoke({"question":qsn+"."+suf,"messages":history.messages})
    history.add_user_message(qsn)
    history.add_ai_message(response)
    return response
