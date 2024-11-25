from typing import List, Dict
import os

def load_documents(file_paths: List[str]) -> List[Dict[str, str]]:
    """Load documents from text files."""
    documents = []
    
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                doc = {
                    'text': content,
                    'source': file_path,
                    'metadata': {
                        'filename': os.path.basename(file_path)
                    }
                }
                documents.append(doc)
        except Exception as e:
            print(f"Error loading document {file_path}: {str(e)}")
    
    return documents
