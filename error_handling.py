import time

def retry_request(func, max_retries=3, delay=5):
    retries = 0
    while retries < max_retries:
        try:
            return func()
        except Exception as e:
            retries += 1
            print(f"Error occurred: {e}. Retrying ({retries}/{max_retries})...")
            time.sleep(delay)
    raise Exception("Max retries reached. Request failed.")

