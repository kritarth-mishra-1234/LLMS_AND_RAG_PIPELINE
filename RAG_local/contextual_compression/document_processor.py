# document_processor.py
from typing import List, Dict, Any
import os
from config import CHUNK_SIZE, CHUNK_OVERLAP

def load_text(file_path: str) -> tuple[str, Dict[str, Any]]:
    """Load text from file and return content and metadata."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    metadata = {"source": file_path}
    return text, metadata

def split_text(text: str, chunk_size: int = CHUNK_SIZE, 
               chunk_overlap: int = CHUNK_OVERLAP) -> List[str]:
    """Split text into chunks with overlap."""
    if not text:
        return []

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        
        # If not the first chunk, include overlap from previous chunk
        if start > 0:
            chunk = text[start - chunk_overlap:end]
        
        chunks.append(chunk)
        start = end - chunk_overlap
    
    return chunks

def process_documents(file_paths: List[str]) -> List[tuple[str, Dict[str, Any]]]:
    """Process multiple documents and split them into chunks with metadata."""
    processed_chunks = []

    for file_path in file_paths:
        text, base_metadata = load_text(file_path)
        chunks = split_text(text)
        
        for chunk in chunks:
            metadata = {
                **base_metadata,
                "chunk_size": len(chunk)
            }
            processed_chunks.append((chunk, metadata))

    return processed_chunks