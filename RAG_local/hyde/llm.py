import openai
from typing import List
import config

openai.api_key = config.OPENAI_API_KEY

def generate_completions(
    prompt: str,
    n: int = 1,
    temperature: float = 0.7
) -> List[str]:
    """
    Generate completions using OpenAI's API.
    
    Args:
        prompt: Input prompt
        n: Number of completions to generate
        temperature: Sampling temperature
        
    Returns:
        List of generated completions
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            n=n,
            temperature=temperature
        )
        return [choice.message.content for choice in response.choices]
    except Exception as e:
        print(f"Error generating completions: {e}")
        raise