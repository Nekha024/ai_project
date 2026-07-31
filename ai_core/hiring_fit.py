def calculate_hiring_fit(score):

    if score >= 80:
        category = "Excellent Fit"

    elif score >= 65:
        category = "Good Fit"

    elif score >= 50:
        category = "Moderate Fit"

    else:
        category = "Low Fit"

    return {

        "hiring_fit_percentage": score,

        "fit_category": category

    }