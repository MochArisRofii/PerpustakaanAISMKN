from langchain.document_loaders.pdf import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document
from langchain_chroma import Chroma
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from llama_index.core import SimpleDirectoryReader

import os
import shutil

load_dotenv()

PDFPATH = r"./DOCS"

# Loader LlamaIndex
def load_documentdir(path):
    """
    Load PDF documents from the specified directory using PyPDFDirectoryLoader.

    Returns:
        List of Document objects: Loaded PDF documents represented as Langchain Document objects.
    """
     # Initialize file loader with specified directory
    documents_llamaindex = SimpleDirectoryReader(path).load_data()

# Mengonversi ke LangChain Document
    documents_langchain = [
        Document(page_content=doc.text, metadata={"source": doc.extra_info.get("file_name")}) 
        for doc in documents_llamaindex
    ]
    return documents_langchain

# Text Spliter and chunks
def split_text(documents: list[Document]):
    """Split the text of a list of documents into smaller chunks.

    Args:
        documents (list[Document]): A list of documents object containing text to split.
    
    Returns:
        list[Document]: list of document objects representing the split text chunks.
    """
    # initialize text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300, #size of each chunk in characters
        chunk_overlap=75, # overlap between consecutive chunks 100 changed to 75
        length_function=len, #function to compute the length of the text
        add_start_index=True, #Flag to add start index to each chunk
    )
    # Split documents into smaller chunks using text splitter
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    # Print example of page content and metadata for a chunk
    document = chunks[0]
    print(document.page_content)
    print(document.metadata)

    return chunks # Return the list of split text chunks

# Save to chroma
CHROMA_PATH = r"./db"
def save_to_chroma(chunks: list[Document]):
  """
  Save the given list of Document objects to a Chroma database.
  Args:
  chunks (list[Document]): List of Document objects representing text chunks to save.
  Returns:
  None
  """

  # Clear out the existing database directory if it exists
  if os.path.exists(CHROMA_PATH):
    shutil.rmtree(CHROMA_PATH)

  # Create a new Chroma database from the documents using OpenAI embeddings
  db = Chroma.from_documents(
    chunks,
    OpenAIEmbeddings(openai_api_key=os.getenv('OPENAI_API_KEY'), allowed_special={'<|endoftext|>'}),
    persist_directory=CHROMA_PATH
  )

  # Persist the database to disk
  db
  print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

def generate_data_store(path):
  """
  Function to generate vector database in chroma from documents.
  """
  documents = load_documentdir(f"{path}") # Load documents from a source
  chunks = split_text(documents) # Split documents into manageable chunks
  save_to_chroma(chunks) # Save the processed data to a data store

generate_data_store(PDFPATH)

