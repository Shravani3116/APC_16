def eligibility(attended, total):
    percentage = (attended / total) * 100

    if percentage >= 75:
        return "Eligible"
    else:
        return "Not Eligible"