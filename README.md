# **🤖 AI Data Retriever & Table Completer**
"AI Data Retriever" leverages the Gemini API and web search to automate data retrieval and table completion. This intuitive dashboard allows users to upload datasets, define custom queries, and extract structured insights with AI-powered precision.

# **📜 Introduction**
This project includes a Flask-based dashboard and a modular Python backend. Users can upload CSV files or link Google Sheets, define prompts for automated web searches, and retrieve structured data. Leveraging the Gemini API and SerpAPI, the app auto-completes table data and delivers actionable outputs.

Below are the step-by-step instructions to set up and run the project.

# **🚀 Step 1: Setting Up API Keys**
🔑 1. Create a SerpAPI Key
Follow this video tutorial to create your SerpAPI key:

[![Scraping Google Maps using SerpApi and Node.js](https://i.ytimg.com/an_webp/emFKwWLR4Ok/mqdefault_6s.webp?du=3000&sqp=CLD5-roG&rs=AOn4CLCVT_sGzrCY9WLUEa_vUrWtozMbug
)](https://www.youtube.com/results?search_query=Scraping+Google+Maps+using+SerpApi+and+Node.js)

Save your API Key for later use.

# **🔑 2. Create a Gemini API Key**
Follow this video tutorial to create your Gemini API key:

[![Gemini AI API with Python Latest Tutorial](https://i.ytimg.com/an_webp/pTcunloZ-_o/mqdefault_6s.webp?du=3000&sqp=CMj4-roG&rs=AOn4CLDTZRbyBRlcGbM5ltL3Ket92j3iTw
)](https://www.youtube.com/watch?v=pTcunloZ-_o)

Save your API Key for later use.

# **📝 Insert API Keys in app.py**
Open app.py and:

Paste the SerpAPI key at line 10:
```python
SERP_API_KEY = "your-serpapi-key"
Paste the Gemini API key at line 11:
```
```python
GENIMI_API_KEY = "your-gemini-api-key"
```

# **⚙️ Step 2: Install Dependencies**
🛠 Install Required Libraries
Run the following command to install all the necessary libraries:

```python
pip install flask pandas google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client serpapi gemini-api
```

# **📂 Step 3: Project Structure
Folder Overview:-
```python
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
```

# **🔧 Step 4: Setting Up the Google Sheets API**
🔑 1. Enable Google Sheets API
Follow this tutorial to enable the Google Sheets API and download the credentials JSON file.

[![Automate Google Sheets With Python - Google Sheets API Tutorial](https://i.ytimg.com/an_webp/zCEJurLGFRk/mqdefault_6s.webp?du=3000&sqp=CIzp-roG&rs=AOn4CLCicMQoQQHoe653Bqwh0sTClU-9Cg
)](https://www.youtube.com/watch?v=zCEJurLGFRk)

Save the credentials file as credentials.json in the project root.

📝 Modify google_sheets_handler.py
Update the following variables in the google_sheets_handler.py file:

```python
CREDENTIALS_FILE = "path/to/credentials.json"
SCOPE = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
```

# **🌐 Step 5: Running the Project**
1. Start the Flask App
Navigate to the project folder in your terminal and run:

```python
python app.py
```
![image](https://github.com/user-attachments/assets/6301fcb5-31ce-4e31-a920-9b3079e15a71)

# **2. Access the Dashboard**
Open your browser and go to:
http://127.0.0.1:5000/

![image](https://github.com/user-attachments/assets/093f95f0-4a4c-4d88-86dd-3c12d3de9f1d)


# **🎨 Step 6: Using the Dashboard**
📂 1. Upload Your Data
Use the "Upload File" button to upload a CSV file.
Or, connect to a Google Sheet by entering the sheet URL.
# **📋 2. Define the Main Column**
Select the primary column (e.g., company names) to perform searches for each entity.


# **💡 3. Input Your Query Template**
Define a custom query with placeholders, e.g.,: 

```python
Get me the official email address of {entity}.
```

# **🔍 4. Start the Search**
Click "Search" to perform automated web searches and retrieve data. 

![image](https://github.com/user-attachments/assets/8ce75552-f06a-459d-970d-ab5db653a4e2)

# **📥 Step 7: Downloading Results**
📊 View Results
The dashboard will display the retrieved data in a structured table.
📂 Download Results
Use the "Download CSV" button to save the results locally.
Or, update your Google Sheet with the retrieved data. 
![image](https://github.com/user-attachments/assets/edccf348-77dd-4189-93f3-6d31c6686bb9)

# **📋 Conclusion**
By following these steps, you can successfully set up and run the AI-powered data retriever. With this project, users can automate web searches, retrieve structured data, and complete tables using AI. 
