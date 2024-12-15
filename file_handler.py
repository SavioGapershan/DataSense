import pandas as pd

def handle_file_upload(file):
    try:
        return pd.read_csv(file)
    except Exception as e:
        raise ValueError(f"Error reading CSV file: {e}")

