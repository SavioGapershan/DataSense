🤖 AI Data Retriever & Table Completer
"AI Data Retriever" leverages the Gemini API and web search to automate data retrieval and table completion. This intuitive dashboard allows users to upload datasets, define custom queries, and extract structured insights with AI-powered precision. 

📜 Introduction
This project includes a Flask-based dashboard and a modular Python backend. Users can upload CSV files or link Google Sheets, define prompts for automated web searches, and retrieve structured data. Leveraging the Gemini API and SerpAPI, the app auto-completes table data and delivers actionable outputs.

Below are the step-by-step instructions to set up and run the project.

🚀 Step 1: Setting Up API Keys
🔑 1. Create a SerpAPI Key
Follow this video tutorial to create your SerpAPI key:




Save your API Key for later use.

🔑 2. Create a Gemini API Key
Follow this video tutorial to create your Gemini API key: 







Save your API Key for later use.

📝 Insert API Keys in app.py
Open app.py and:

Paste the SerpAPI key at line 10:
```python
SERP_API_KEY = "your-serpapi-key"
```
Paste the Gemini API key at line 11: 
```python
GENIMI_API_KEY = "your-gemini-api-key"
```

⚙️ Step 2: Install Dependencies
🛠 Install Required Libraries
Run the following command to install all the necessary libraries:
```python
pip install flask pandas google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client serpapi gemini-api
```

📂 Step 3: Project Structure
Folder Overview
📦 project-folder
│
├── 📂 modules
│   ├── google_sheets_handler.py    # Handles Google Sheets API integration
│   ├── web_search.py               # Automates web searches using SerpAPI
│   └── data_processor.py           # Processes and structures retrieved data
│
├── app.py                          # Main Flask app for the dashboard
├── templates/
│   └── index.html                  # HTML template for the dashboard UI
├── requirements.txt                # Python dependencies list
└── README.md                       # Project documentation

🔧 Step 4: Setting Up the Google Sheets API
🔑 1. Enable Google Sheets API
Follow this tutorial to enable the Google Sheets API and download the credentials JSON file.







Save the credentials file as credentials.json in the project root.

📝 Modify google_sheets_handler.py
Update the following variables in the google_sheets_handler.py file:

CREDENTIALS_FILE = "path/to/credentials.json"
SCOPE = ["https://www.googleapis.com/auth/spreadsheets.readonly"]




Here's the detailed and colorful README file for your project:

🤖 AI Data Retriever & Table Completer
"AI Data Retriever" leverages the Gemini API and web search to automate data retrieval and table completion. This intuitive dashboard allows users to upload datasets, define custom queries, and extract structured insights with AI-powered precision.

📜 Introduction
This project includes a Flask-based dashboard and a modular Python backend. Users can upload CSV files or link Google Sheets, define prompts for automated web searches, and retrieve structured data. Leveraging the Gemini API and SerpAPI, the app auto-completes table data and delivers actionable outputs.

Below are the step-by-step instructions to set up and run the project.

🚀 Step 1: Setting Up API Keys
🔑 1. Create a SerpAPI Key
Follow this video tutorial to create your SerpAPI key:


Save your API Key for later use.

🔑 2. Create a Gemini API Key
Follow this video tutorial to create your Gemini API key:


Save your API Key for later use.

📝 Insert API Keys in app.py
Open app.py and:

Paste the SerpAPI key at line 10:
python
Copy code
SERP_API_KEY = "your-serpapi-key"
Paste the Gemini API key at line 11:
python
Copy code
GENIMI_API_KEY = "your-gemini-api-key"
⚙️ Step 2: Install Dependencies
🛠 Install Required Libraries
Run the following command to install all the necessary libraries:

bash
Copy code
pip install flask pandas google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client serpapi gemini-api
📂 Step 3: Project Structure
Folder Overview
plaintext
Copy code
📦 project-folder
│
├── 📂 modules
│   ├── google_sheets_handler.py    # Handles Google Sheets API integration
│   ├── web_search.py               # Automates web searches using SerpAPI
│   └── data_processor.py           # Processes and structures retrieved data
│
├── app.py                          # Main Flask app for the dashboard
├── templates/
│   └── index.html                  # HTML template for the dashboard UI
├── requirements.txt                # Python dependencies list
└── README.md                       # Project documentation
🔧 Step 4: Setting Up the Google Sheets API
🔑 1. Enable Google Sheets API
Follow this tutorial to enable the Google Sheets API and download the credentials JSON file.

Save the credentials file as credentials.json in the project root.

📝 Modify google_sheets_handler.py
Update the following variables in the google_sheets_handler.py file:

```python
CREDENTIALS_FILE = "path/to/credentials.json"
SCOPE = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
```

🌐 Step 5: Running the Project
1. Start the Flask App
Navigate to the project folder in your terminal and run:

```python
python app.py
```

2. Access the Dashboard
Open your browser and go to:
http://127.0.0.1:5000/

🎨 Step 6: Using the Dashboard
📂 1. Upload Your Data
Use the "Upload File" button to upload a CSV file.
Or, connect to a Google Sheet by entering the sheet URL.
📋 2. Define the Main Column
Select the primary column (e.g., company names) to perform searches for each entity.
💡 3. Input Your Query Template
Define a custom query with placeholders, e.g.,: 

```python
Get me the official email address of {entity}.
```

🔍 4. Start the Search
Click "Search" to perform automated web searches and retrieve data. 

📥 Step 7: Downloading Results
📊 View Results
The dashboard will display the retrieved data in a structured table.
📂 Download Results
Use the "Download CSV" button to save the results locally.
Or, update your Google Sheet with the retrieved data. 

📋 Conclusion
By following these steps, you can successfully set up and run the AI-powered data retriever. With this project, users can automate web searches, retrieve structured data, and complete tables using AI. 

📽️ Demo Video
Watch this step-by-step guide to see the project in action:

