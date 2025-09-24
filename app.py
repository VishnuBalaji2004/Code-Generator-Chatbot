from dotenv import load_dotenv
import streamlit as st
import chain

load_dotenv()

def code_generator():
    """
    Code Generator Bot
    """
    with st.form("Code_Generator"):
        st.write("## Code Generator Bot")
        language= st.text_input("Enter the Programming Language")
        problem_statement = st.text_input("Enter the Problem Statement")
        submitted = st.form_submit_button("submit",type="primary")
        if(submitted):
            response =chain.generate_code(language,problem_statement)
            st.info(response)

code_generator()

