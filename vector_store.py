from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore

import os
import time
from dotenv import load_dotenv
from data_loader import docs, embeddings

load_dotenv()

# Initialize client with modern SDK
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

index_name = "langchain-demo"
dimension = 768  # Verify with your embedding model

# Create index if missing
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=dimension,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
    # Wait for index readiness
    while not pc.describe_index(index_name).status.ready:
        time.sleep(5)

# Initialize vector store CORRECTLY
docsearch = PineconeVectorStore.from_documents(
    documents=docs,
    embedding=embeddings,
    index_name=index_name
)
