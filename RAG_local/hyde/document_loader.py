# document_loader.py
from typing import List, Dict, Any, Tuple

def load_text_file(file_path: str) -> Tuple[str, Dict[str, Any]]:
    """
    Load text from a file and return content and metadata.
    
    Args:
        file_path: Path to the text file
        
    Returns:
        Tuple of (text content, metadata dictionary)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            
        metadata = {
            'source': file_path,
            'filename': file_path.split('/')[-1]
        }
        
        return text, metadata
    except Exception as e:
        print(f"Error loading file {file_path}: {e}")
        raise

def load_documents(file_paths: List[str]) -> List[Tuple[str, Dict[str, Any]]]:
    """
    Load multiple text files.
    
    Args:
        file_paths: List of paths to text files
        
    Returns:
        List of tuples containing (text content, metadata)
    """
    documents = []
    for path in file_paths:
        try:
            doc = load_text_file(path)
            documents.append(doc)
        except Exception as e:
            print(f"Skipping file {path} due to error: {e}")
    return documents