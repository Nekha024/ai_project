import re
import time
import threading

from functools import lru_cache
from concurrent.futures import ThreadPoolExecutor


# -------------------------------
# Cached Text Cleaning
# -------------------------------
@lru_cache(maxsize=1000)
def clean_text_cached(text):

    text = text.lower()

    text = re.sub(
        r"[^a-z0-9\s\.\,\-]",
        "",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text


# -------------------------------
# Parallel Resume Processing
# -------------------------------
def process_resumes_parallel(
    resume_texts,
    process_function
):

    results = []

    with ThreadPoolExecutor(max_workers=4) as executor:

        futures = [

            executor.submit(
                process_function,
                text
            )

            for text in resume_texts
        ]

        for future in futures:

            results.append(
                future.result()
            )

    return results


# -------------------------------
# Lightweight Skill Extraction
# -------------------------------
SKILLS = [
    "python",
    "java",
    "react",
    "node",
    "sql",
    "django"
]


def fast_skill_extract(text):

    text = clean_text_cached(text)

    return [

        skill for skill in SKILLS

        if skill in text
    ]


# -------------------------------
# Batch Processing
# -------------------------------
def batch_process(
    data,
    batch_size=10
):

    for i in range(
        0,
        len(data),
        batch_size
    ):

        yield data[i:i + batch_size]


# -------------------------------
# Noisy Resume Cleaning
# -------------------------------
def clean_noisy_resume(text):

    text = clean_text_cached(text)

    # Remove repeated characters
    text = re.sub(
        r"(.)\1{2,}",
        r"\1",
        text
    )

    # Remove repeated punctuation
    text = re.sub(
        r"[\.\,\-]{2,}",
        "",
        text
    )

    return text


# -------------------------------
# Safe Execution
# -------------------------------
def safe_execute(
    func,
    data
):

    try:

        return func(data)

    except Exception as e:

        return {
            "error": str(e)
        }


# -------------------------------
# Retry Mechanism
# -------------------------------
def retry(
    func,
    data,
    retries=3
):

    for attempt in range(retries):

        try:

            return func(data)

        except:

            time.sleep(1)

    return {
        "error": "Failed after retries"
    }


# -------------------------------
# Windows-Safe Timeout Wrapper
# -------------------------------
def run_with_timeout(
    func,
    data,
    timeout=5
):

    result = {}

    def target():

        try:

            result["value"] = func(data)

        except Exception as e:

            result["error"] = str(e)

    thread = threading.Thread(
        target=target
    )

    thread.start()

    thread.join(timeout)

    if thread.is_alive():

        return {
            "error": "Timeout"
        }

    return result.get(
        "value",
        result
    )


# -------------------------------
# Example Execution
# -------------------------------
if __name__ == "__main__":

    resumes = [

        "Python developer!!! with Django---- experience",

        "React developer..... Node.js expert"
    ]

    cleaned = [

        clean_noisy_resume(r)

        for r in resumes
    ]

    results = process_resumes_parallel(
        cleaned,
        fast_skill_extract
    )

    print("\nOptimized Processing Result:\n")

    print(results)