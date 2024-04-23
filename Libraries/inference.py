"""
This file contains the inference functions for the different models.
"""

# Config
from .config import OPENAI_API_KEY, TOGETHER_API_KEY, GROQ_API_KEY, OPENROUTER_API_KEY

# Libraries
import requests
import json


# Completion Endpoints
url_local = "http://localhost:8881/completion"
url_openai = "https://api.openai.com/v1/chat/completions"
url_together = "https://api.together.xyz/v1/chat/completions"
url_openrouter = "https://openrouter.ai/api/v1/chat/completions"
url_groq = "https://api.groq.com/openai/v1/chat/completions"


# Headers
headers_local = {
    'Content-Type': 'application/json'    
}

headers_openai = {
    'Content-Type': 'application/json',
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}

headers_groq = {
    'Content-Type': 'application/json',
    "Authorization": f"Bearer {GROQ_API_KEY}"
}

headers_together = {
    'Content-Type': 'application/json',
    "Authorization": f"Bearer {TOGETHER_API_KEY}"    
}

headers_openrouter = {
    'Content-Type': 'application/json',
    "Authorization": f"Bearer {OPENROUTER_API_KEY}"    
}


def complete_local( prompt, model=None, max_tokens=256 ):
    # a llama.cpp server (ref: https://github.com/ggerganov/llama.cpp/tree/master/examples/server)

    # Define the payload
    payload = {
        "prompt": prompt,
        "n_predict": max_tokens,
        "temperature": 0.0
    }

    # Send the POST request
    response = requests.post(url_local, headers=headers_local, data=json.dumps(payload))
    try:
        response = response.json()
    except:
        print('ERROR: Could not parse response')
        return None

    # Validate
    if 'content' not in response: 
        print(response)
        return None

    # Extract completion
    completion = response["content"]
    
    return completion


def complete_openai( messages, model, max_tokens=256 ):
    return complete_remote( messages, model, max_tokens, url_openai, headers_openai )

def complete_together( messages, model, max_tokens=256 ):
    return complete_remote( messages, model, max_tokens, url_together, headers_together )

def complete_openrouter( messages, model, max_tokens=256 ):
    return complete_remote( messages, model, max_tokens, url_openrouter, headers_openrouter )

def complete_groq( messages, model, max_tokens=256 ):
    return complete_remote( messages, model, max_tokens, url_groq, headers_groq )

def complete_remote( messages, model, max_tokens=256, url=None, headers=None ):

    # Define the payload
    payload = {
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": 0.0,
        "model": model,
        "seed": 42
    }

    # Send the POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    try:
        response = response.json()
    except:
        print('ERROR: Could not parse response')
        return None

    # Validate
    if 'choices' not in response: 
        print(response)
        return None

    # Extract completion
    completion = response['choices'][0]['message']['content'].strip()

    return completion
