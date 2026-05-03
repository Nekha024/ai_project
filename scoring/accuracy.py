import sys
import os
import json

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from parsers.section_classifier import segment_resume

# sklearn metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def evaluate():
    # ✅ Better path handling (fixes file issues)
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(BASE_DIR, "data", "outputs/test_samples.json")

    with open(file_path, "r") as f:
        samples = json.load(f)

    labels = ["skills", "experience", "education", "projects", "certifications"]

    # Store per-label values
    y_true_all = {label: [] for label in labels}
    y_pred_all = {label: [] for label in labels}

    # Overall lists
    all_expected = []
    all_predicted = []

    print("\n===== SECTION DETECTION REPORT =====\n")

    for i, sample in enumerate(samples):
        text = sample["text"]
        expected = sample["expected"]
        predicted = list(segment_resume(text).keys())

        print(f"Sample {i+1}")
        print(f"Expected : {expected}")
        print(f"Predicted: {predicted}")
        print("-" * 40)

        for label in labels:
            true_val = 1 if label in expected else 0
            pred_val = 1 if label in predicted else 0

            y_true_all[label].append(true_val)
            y_pred_all[label].append(pred_val)

            all_expected.append(true_val)
            all_predicted.append(pred_val)

    # ✅ PER-SECTION METRICS
    print("\n===== PER-SECTION METRICS =====\n")

    for label in labels:
        precision = precision_score(y_true_all[label], y_pred_all[label], zero_division=0)
        recall = recall_score(y_true_all[label], y_pred_all[label], zero_division=0)
        f1 = f1_score(y_true_all[label], y_pred_all[label], zero_division=0)

        print(f"{label.capitalize():15} | Precision: {precision:.2f} | Recall: {recall:.2f} | F1: {f1:.2f}")

    # ✅ OVERALL METRICS (your original logic)
    accuracy = accuracy_score(all_expected, all_predicted)
    precision = precision_score(all_expected, all_predicted, zero_division=0)
    recall = recall_score(all_expected, all_predicted, zero_division=0)
    f1 = f1_score(all_expected, all_predicted, zero_division=0)

    print("\n===== OVERALL METRICS =====\n")
    print(f"Accuracy : {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall   : {recall:.2f}")
    print(f"F1 Score : {f1:.2f}")
    print("\n=============================\n")


if __name__ == "__main__":
    evaluate()