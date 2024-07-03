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

url=os.getenv("QDRANT_URL")
api_key=os.getenv("QDRANT_API_KEY")
collection_name=os.getenv("COLLECTION_NAME")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")





@st.cache_resource
def formated_examples(qsn):
    client = QdrantClient(url=url, api_key=api_key)
    qdrant = Qdrant(client, collection_name, embeddings)
    example_selector = qdrant.similarity_search(qsn,k=5)

    formatted_examples = [
        {"input": example.metadata["input"], "query": example.metadata["query"]}
        for example in example_selector
    ]

    return formatted_examples
