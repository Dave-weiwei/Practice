def grade(score):
    if not isinstance(score, (int, float)):
        raise ValueError("分數必須是數字")
    if score < 0 or score > 100:
        raise ValueError("分數必須在 0~100 之間")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"