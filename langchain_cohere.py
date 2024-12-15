import os
import csv
from dotenv import load_dotenv
from cohere import Client

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

if COHERE_API_KEY is None:
    raise ValueError("API key is missing. Please check the .env file.")

# Initialize Cohere client with the API key
co = Client(COHERE_API_KEY)

# Example function to use Cohere's API to generate text
def generate_text_with_cohere(prompt: str, max_tokens: int = 50):
    try:
        response = co.generate(
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response.generations[0].text  # Corrected way to access the generated text
    except Exception as e:
        print(f"Error generating text: {e}")
        return None

# Save the output to a CSV file
def save_to_csv(data, filename="output.csv"):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Query", "Response"])  # Add header row
            for row in data:
                writer.writerow(row)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

# Example usage
if __name__ == "__main__":
    queries = ["Tell me a joke", "Explain quantum physics in simple terms", "What is AI?"]
    results = []

    for query in queries:
        result = generate_text_with_cohere(query)
        if result:
            results.append([query, result])

    # Save results to CSV
    if results:
        save_to_csv(results)
    else:
        print("No results to save.")

