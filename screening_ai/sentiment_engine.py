POSITIVE_WORDS = [
    "good", "great", "confident",
    "skilled", "experienced", "strong"
]

NEGATIVE_WORDS = [
    "weak", "bad", "problem",
    "difficult", "struggle", "not sure"
]

def detect_sentiment(text):

    text = text.lower()

    pos = sum(word in text for word in POSITIVE_WORDS)
    neg = sum(word in text for word in NEGATIVE_WORDS)

    if pos > neg:
        return {
            "sentiment": "Positive",
            "sentiment_score": min(pos / 5, 1.0)
        }

    elif neg > pos:
        return {
            "sentiment": "Negative",
            "sentiment_score": min(neg / 5, 1.0)
        }

    return {
        "sentiment": "Neutral",
        "sentiment_score": 0.5
    }