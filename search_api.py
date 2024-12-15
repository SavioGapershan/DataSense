import requests
import os

SERP_API_KEY = os.getenv("SERPAPI_KEY")

def perform_search(entities, query):
    search_results = []
    for entity in entities:
        formatted_query = query.replace("{entity}", entity)
        response = requests.get(
            "https://serpapi.com/search",
            params={"q": formatted_query, "api_key": SERP_API_KEY}
        )
        response_data = response.json()
        if "organic_results" in response_data:
            search_results.append({
                "entity": entity,
                "results": response_data["organic_results"]
            })
    return search_results

