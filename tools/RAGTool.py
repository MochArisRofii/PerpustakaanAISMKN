from crewai.tools import BaseTool
from langchain.embeddings import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Menyusun API Key dari .env
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")  # Pastikan nama kunci sesuai dengan yang ada di .env
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")  # Memastikan OpenAI API key tersedia

# Membuat instance TavilySearchResults untuk pencarian
from langchain_community.tools import TavilySearchResults
SearchTool = TavilySearchResults(k=5)

CHROMA_PATH = r"./db"  # Tentukan path ke Chroma DB Anda

class RAGTool(BaseTool):
    name: str = "RAGTool"
    description: str = "Search the vector db for related information"

    def _run(self, query: str) -> str:
        """
        Search related information from queries
        """
        # Memastikan API key tersedia untuk OpenAI
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OPENAI_API_KEY tidak ditemukan di variabel lingkungan.")

        # Membuat fungsi embedding untuk OpenAI
        embedding_function = OpenAIEmbeddings(openai_api_key=openai_api_key, allowed_special={'<|endoftext|>'})

        # Membuka Chroma DB
        db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

        try:
            # Melakukan pencarian dan mengambil relevansi hasil pencarian
            results = db.similarity_search_with_relevance_scores(query, k=4)
            
            # Jika hasil ditemukan, kembalikan informasi yang relevan
            if results:
                return "\n".join([f"Score: {score}, Text: {doc}" for doc, score in results])
            else:
                return "Tidak ada informasi yang relevan ditemukan."
        except Exception as e:
            return f"Error saat mencari data: {str(e)}"

