import time


def retry_request(func, retries=3):
    for attempt in range(retries):
        try:
            return func()
        except Exception:
            time.sleep(1)

    return {"error": "Max retries exceeded"}