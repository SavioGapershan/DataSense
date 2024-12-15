from utils.groq_api import extract_information
from utils.search_api import perform_search
import pandas as pd
import streamlit as st

# Initialize Streamlit App
st.title("AI-Powered Data Enhancer")
st.write("Upload your data file or connect to Google Sheets, provide a query, and extract enriched information.")

# File upload or Google Sheets connection
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data Preview")
    st.dataframe(data)
else:
    st.error("Please upload a CSV file to proceed.")
    st.stop()

# Select a column for the main entities
column_name = st.selectbox("Select the column containing entities:", data.columns)
if not column_name:
    st.error("Please select a column containing entities.")
    st.stop()

entities = data[column_name].dropna().tolist()  # Extract non-empty entities from the selected column

# User query input
query = st.text_input("Enter your query (e.g., Get the CEO name of {entity}):")

if st.button("Run Query"):
    if not query:
        st.error("Please enter a query.")
        st.stop()

    with st.spinner("Performing Web Search..."):
        search_results = perform_search(entities, query)

    with st.spinner("Extracting Information..."):
        extracted_data = extract_information(search_results, query)

    # Update the DataFrame with the results
    for idx, entity_data in enumerate(extracted_data):
        for key, value in entity_data.items():
            if key not in data.columns:
                data[key] = None  # Add a new column if it doesn't exist
            data.at[idx, key] = value

    st.write("### Updated Data")
    st.dataframe(data)

    # Download CSV
    csv_data = data.to_csv(index=False)
    st.download_button("Download Updated Data as CSV", csv_data, "updated_data.csv")

