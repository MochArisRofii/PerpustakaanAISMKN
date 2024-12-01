import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

load_dotenv()


class Static:
    def llm():
        return ChatOpenAI(
            model=os.getenv("OPENAI_MODEL_NAME"),
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0.2,
        )

    def pageConfig():
        return st.set_page_config(
            page_title="SKABOOK",
            page_icon="🎓",
            layout="centered",
        )

    def logo():
        # Menampilkan logo dengan animasi fade-in
        return st.image("./logo.png")

    def pageTitle():

        return st.markdown(
            """
            <div class="header-container" style="margin-top: 1%;">
                <h1 class="header-title">SKABOOK</h1>
                <p class="header-subtitle">Dikembangkan oleh</p>
                <p class="header-team">SMKN 9 MALANG Data Science ✨</p>
            </div>
            <style>
                @keyframes slideIn {
                    0% { transform: translateY(50px); opacity: 0; }
                    100% { transform: translateY(0); opacity: 1; }
                }

                @keyframes textColorChange {
                    0% { color: #FF5722; }
                    50% { color: #FF9800; }
                    100% { color: #F44336; }
                }
            </style>
        """,
            unsafe_allow_html=True,
        )

    def pageCss():
        # Desain dengan fokus pada transisi lembut dan efek hover yang menarik
        return st.markdown(
            """
            <style>
                /* Body styling */
                body {
                    font-family: 'Arial', sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #F3F4F6;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }

                /* Button with hover animation */
                .stButton button {
                    background-color: #FF5722;
                    color: white;
                    font-size: 1.1rem;
                    font-weight: 600;
                    padding: 14px 24px;
                    border-radius: 30px;
                    border: none;
                    box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
                    cursor: pointer;
                    transition: all 0.3s ease;
                }

                .stButton button:hover {
                    transform: translateY(-5px);
                    box-shadow: 0px 10px 25px rgba(0, 0, 0, 0.3);
                    background-color: #FF7043;
                }

                /* Input field with smooth focus effect */
                .stTextInput input {
                    padding: 12px;
                    font-size: 1rem;
                    border-radius: 10px;
                    border: 2px solid #FF5722;
                    width: 100%;
                    transition: border-color 0.3s ease, box-shadow 0.3s ease;
                }

                .stTextInput input:focus {
                    border-color: #FF7043;
                    box-shadow: 0 0 10px rgba(255, 112, 67, 0.5);
                }

                /* Container for the result with smooth shadow and hover effect */
                .result-container {
                    padding: 24px;
                    background-color: #fff;
                    box-shadow: 0 4px 25px rgba(0, 0, 0, 0.1);
                    border-radius: 12px;
                    margin-top: 30px;
                    transition: transform 0.3s ease-in-out, box-shadow 0.3s ease;
                }

                .result-container:hover {
                    transform: translateY(-5px);
                    box-shadow: 0px 6px 30px rgba(0, 0, 0, 0.15);
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
