# src/retrievers/ensemble_retriever.py
import numpy as np

def get_ensemble_documents(retriever_results, weights):
    """Combine results from multiple retrievers using weights."""
    if len(retriever_results) != len(weights):
        raise ValueError("Number of retriever results must match number of weights")
    if not np.isclose(sum(weights), 1.0):
        raise ValueError("Weights must sum to 1")
    
    # Adjust scores by weight
    weighted_results = []
    for results, weight in zip(retriever_results, weights):
        for result in results:
            weighted_results.append({
                "text": result["text"],
                "score": result["score"] * weight
            })

    # Combine and deduplicate results
    unique_results = {}
    for result in weighted_results:
        text = result["text"]
        if text in unique_results:
            unique_results[text]["score"] += result["score"]
        else:
            unique_results[text] = result

    # Sort by combined score
    return sorted(
        unique_results.values(),
        key=lambda x: x["score"],
        reverse=True
    )