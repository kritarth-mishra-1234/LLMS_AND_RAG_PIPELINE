# text_splitter.py
def split_text(
    text: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 0,
    separator: str = "\n\n"
) -> List[str]:
    """
    Split text into chunks of specified size with optional overlap.
    
    Args:
        text: Text to split
        chunk_size: Maximum size of each chunk
        chunk_overlap: Number of characters to overlap between chunks
        separator: String to use as separator when splitting
        
    Returns:
        List of text chunks
    """
    # Split text into initial chunks using separator
    chunks = text.split(separator)
    chunks = [chunk.strip() for chunk in chunks if chunk.strip()]
    
    # Further split chunks that are too large
    result = []
    current_chunk = ""
    
    for chunk in chunks:
        if len(current_chunk) + len(chunk) <= chunk_size:
            current_chunk += (separator if current_chunk else "") + chunk
        else:
            if current_chunk:
                result.append(current_chunk)
            current_chunk = chunk
            
            # Split large chunks
            while len(current_chunk) > chunk_size:
                split_point = current_chunk.rfind(". ", 0, chunk_size)
                if split_point == -1:
                    split_point = current_chunk.rfind(" ", 0, chunk_size)
                if split_point == -1:
                    split_point = chunk_size
                    
                result.append(current_chunk[:split_point].strip())
                current_chunk = current_chunk[split_point-chunk_overlap:].strip()
    
    if current_chunk:
        result.append(current_chunk)
    
    return result

def split_document(
    text: str,
    metadata: Dict[str, Any],
    chunk_size: int = 1000,
    chunk_overlap: int = 0
) -> List[Tuple[str, Dict[str, Any]]]:
    """
    Split a document into chunks while preserving metadata.
    
    Args:
        text: Document text
        metadata: Document metadata
        chunk_size: Maximum size of each chunk
        chunk_overlap: Number of characters to overlap between chunks
        
    Returns:
        List of tuples containing (chunk text, chunk metadata)
    """
    chunks = split_text(text, chunk_size, chunk_overlap)
    result = []
    
    for i, chunk in enumerate(chunks):
        chunk_metadata = {
            **metadata,
            'chunk_index': i,
            'chunk_total': len(chunks)
        }
        result.append((chunk, chunk_metadata))
    
    return result

def process_documents(
    documents: List[Tuple[str, Dict[str, Any]]],
    chunk_size: int = 1000,
    chunk_overlap: int = 0
) -> List[Tuple[str, Dict[str, Any]]]:
    """
    Process multiple documents by splitting them into chunks.
    
    Args:
        documents: List of (text, metadata) tuples
        chunk_size: Maximum size of each chunk
        chunk_overlap: Number of characters to overlap between chunks
        
    Returns:
        List of (chunk text, chunk metadata) tuples
    """
    processed_docs = []
    for text, metadata in documents:
        chunks = split_document(text, metadata, chunk_size, chunk_overlap)
        processed_docs.extend(chunks)
    return processed_docs