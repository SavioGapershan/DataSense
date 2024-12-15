from groq import Groq
import os

# Initialize Groq API Client
def get_groq_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is not set in environment variables.")
    return Groq(api_key=api_key)

def extract_information(search_results, query):
    """
    Use Groq API to extract the required information for each entity.
    
    Args:
    - search_results (list): List of search results for each entity.
    - query (str): Query to extract the required information.
    
    Returns:
    - List of dictionaries containing extracted information.
    """
    client = get_groq_client()
    extracted_data = []

    for result in search_results:
        entity = result["entity"]
        documents = [doc["snippet"] for doc in result["results"] if "snippet" in doc]

        if not documents:
            extracted_data.append({"entity": entity, "error": "No data found"})
            continue

        # Prepare the Groq messages
        messages = [
            {"role": "system", "content": "You are an expert data extractor. Please extract precise information."},
            {"role": "user", "content": f"Extract the following information for {entity}: {query}. The documents are: {documents}"}
        ]

        # API Call
        try:
            completion = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=messages,
                temperature=0.7,
                max_tokens=100,
                top_p=1,
                stream=False
            )

            # Process Response
            response = completion.choices[0].message["content"]
            extracted_data.append({"entity": entity, **parse_response(response)})

        except Exception as e:
            extracted_data.append({"entity": entity, "error": str(e)})

    return extracted_data


def parse_response(response):
    """
    Parse Groq API response to extract relevant information.
    
    Args:
    - response (str): Raw response from Groq API.
    
    Returns:
    - Dictionary of extracted key-value pairs.
    """
    parsed_data = {}
    lines = response.split("\n")
    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            parsed_data[key.strip()] = value.strip()
    return parsed_data

