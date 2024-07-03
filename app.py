import streamlit as st


from main import run_chain
from db import create_tables


create_tables()
st.title("text2sql chatbot")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
    

if prompt:=st.chat_input("what's up"):

    st.session_state.messages.append({"role":"user",
                                        "content":prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Generating response..."):
        with st.chat_message("assistant"):
            response=run_chain(prompt,st.session_state.messages)
            st.markdown(response)
    st.session_state.messages.append({"role":"assistant","content":response})
