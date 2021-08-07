def heart_rate_rank(current, athlete, excellent, good, above, average, below, poor):
    if current <= athlete:
        return "danger"
    elif athlete <= current < excellent:
        return "athlete"
    elif excellent <= current < good:
        return "excellent"
    elif good <= current < above:
        return "good"
    elif above <= current < average:
        return "above average"
    elif average <= current < below:
        return "average"
    elif below <= current < poor:
        return "below average"
    elif poor <= current:
        return "poor"


def blood_oxygen_levels_rank(blood_oxygen_levels):
    if 100 >= blood_oxygen_levels > 95:
        return "normal"
    elif 95 >= blood_oxygen_levels > 90:
        return "concerning"
    elif 90 >= blood_oxygen_levels:
        return "danger"


def male_heart_rate_rank_by_age(age, heart_rate):
    if 18 <= age < 26:
        return heart_rate_rank(heart_rate, 49, 56, 62, 66, 70, 74, 82)
    elif 26 <= age < 36:
        return heart_rate_rank(heart_rate, 49, 55, 62, 66, 71, 75, 82)
    elif 36 <= age < 46:
        return heart_rate_rank(heart_rate, 50, 57, 63, 67, 71, 76, 83)
    elif 46 <= age < 56:
        return heart_rate_rank(heart_rate, 50, 58, 64, 68, 72, 77, 84)
    elif 56 <= age < 65:
        return heart_rate_rank(heart_rate, 51, 57, 62, 68, 72, 76, 82)
    elif 65 <= age:
        return heart_rate_rank(heart_rate, 50, 56, 62, 66, 70, 74, 80)


def female_heart_rate_rank_by_age(age, heart_rate):
    if 18 <= age < 26:
        return heart_rate_rank(heart_rate, 49, 56, 62, 66, 70, 74, 82)
    elif 26 <= age < 36:
        return heart_rate_rank(heart_rate, 54, 60, 65, 69, 73, 77, 83)
    elif 36 <= age < 46:
        return heart_rate_rank(heart_rate, 54, 60, 65, 70, 74, 79, 85)
    elif 46 <= age < 56:
        return heart_rate_rank(heart_rate, 54, 61, 66, 70, 74, 78, 84)
    elif 56 <= age < 65:
        return heart_rate_rank(heart_rate, 54, 60, 65, 69, 74, 78, 84)
    elif 65 <= age:
        return heart_rate_rank(heart_rate, 54, 60, 65, 69, 73, 77, 84)


def check_indicator(age, gender, heart_rate, blood_oxygen_levels):
    if gender == "male":
        heart_status = male_heart_rate_rank_by_age(age, heart_rate)
    else:
        heart_status = female_heart_rate_rank_by_age(age, heart_rate)
    oxygen_status = blood_oxygen_levels_rank(blood_oxygen_levels)

    return heart_status, oxygen_status
