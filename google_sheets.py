import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def connect_google_sheets(sheet_url):
    credentials = Credentials.from_service_account_file("service_account.json")
    service = build("sheets", "v4", credentials=credentials)

    spreadsheet_id = sheet_url.split("/")[5]
    range_name = "Sheet1"
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()

    data = result.get("values", [])
    if not data:
        raise ValueError("No data found in the Google Sheet.")
    return pd.DataFrame(data[1:], columns=data[0])

