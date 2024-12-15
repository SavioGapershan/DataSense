import openai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_information(search_results, query_template):
    """
    Extracts information from search results using a single OpenAI API call.

    Parameters:
    - search_results (list): A list of search results from the web.
    - query_template (str): The user's query template, e.g., "Get the email of {entity}".
    
    Returns:
    - list: A list of extracted information for each entity.
    """
    if not openai.api_key:
        raise ValueError("OpenAI API key not provided. Set it in the .env file or directly in the code.")

    try:
        # Combine all search results into a single prompt
        combined_prompt = "You are a data extraction assistant.\n"
        for i, result in enumerate(search_results):
            combined_prompt += f"\nEntity {i + 1}: {result}\n"
        combined_prompt += f"\nBased on the provided query template: '{query_template}', extract the requested information for each entity."

        # Make a single API call
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" for more accuracy
            messages=[
                {"role": "system", "content": "You are an assistant specialized in data extraction."},
                {"role": "user", "content": combined_prompt}
            ],
            max_tokens=1000,  # Adjust based on your data size
            temperature=0.7
        )

        # Process and split the response into separate rows
        extracted_data = response['choices'][0]['message']['content'].strip().split("\n")
        return [data.strip() for data in extracted_data if data.strip()]
    
    except Exception as e:
        return [f"Error: {str(e)}"]

