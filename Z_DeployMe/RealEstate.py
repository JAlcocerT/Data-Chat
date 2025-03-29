import streamlit as st
import os
from RealEstate_RAG import re_calculator_md_rag
from RealEstate_API import st_openai_md_genai

import UDF_Auth_functions as af

def main():
    if af.login(): #Simple Auth Layer
        rag_mode = os.getenv("RAG_MODE", False)

        if rag_mode and rag_mode.lower() == "true":  # Check if env var exists and is "true"
            re_calculator_md_rag()
        else:
            st_openai_md_genai()

if __name__ == "__main__":
    main()