def evaluate_accuracy(ai_results, hr_results):

    tp = fp = fn = tn = 0

    for ai, hr in zip(ai_results, hr_results):

        if ai == "Shortlisted" and hr == "Shortlisted":
            tp += 1

        elif ai == "Shortlisted" and hr == "Rejected":
            fp += 1

        elif ai == "Rejected" and hr == "Shortlisted":
            fn += 1

        else:
            tn += 1

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    accuracy = (tp + tn) / len(ai_results)

    f1_score = 2 * (precision * recall) / (precision + recall)

    print("Precision:", round(precision * 100, 2), "%")
    print("Recall:", round(recall * 100, 2), "%")
    print("Accuracy:", round(accuracy * 100, 2), "%")
    print("F1 Score:", round(f1_score * 100, 2), "%")


# Sample Testing Data
ai_results = [
    "Shortlisted", "Shortlisted", "Rejected", "Shortlisted",
    "Rejected", "Shortlisted", "Rejected", "Shortlisted"
]

hr_results = [
    "Shortlisted", "Rejected", "Rejected", "Shortlisted",
    "Rejected", "Shortlisted", "Shortlisted", "Shortlisted"
]

evaluate_accuracy(ai_results, hr_results)