import cohere
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
cohere_client = cohere.Client(COHERE_API_KEY)

def extract_information(search_results, query_template):
    """
    Extracts information from the search results using Cohere.

    Parameters:
    - search_results (list): List of web search results for each entity.
    - query_template (str): Query template (e.g., 'Find the CEO name of {entity}').

    Returns:
    - list: Extracted information for each entity.
    """
    if not COHERE_API_KEY:
        raise ValueError("Cohere API key not provided. Set it in the .env file.")

    try:
        # Prepare the prompt to send to Cohere
        prompt = "Extract relevant details from the following search results.\n\n"
        for i, result in enumerate(search_results):
            prompt += f"Search Result {i + 1}: {result.get('snippet', 'No information available')}\n"

        prompt += f"\nQuery Template: {query_template}\nProvide the extracted data for each entity in the query."

        response = cohere_client.generate(
            model="command-xlarge-nightly",
            prompt=prompt,
            max_tokens=1000,
            temperature=0.7
        )
        
        # Split the response into lines and clean the data
        output = response.generations[0].text.strip().split("\n")
        return [data.strip() for data in output if data.strip()]
    except Exception as e:
        return [f"Error: {str(e)}"]

