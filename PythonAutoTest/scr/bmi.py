def bmi_category(height, weight):
    try:
        h= height
        w=weight
        if h <= 0 or w <= 0:
            return "請輸入正確身高體重"
        BMI= w/((h/100)**2)
        if BMI < 18.5:
            return "體重過輕"
        elif BMI <= 23:
            return "正常"
        elif BMI <= 25:
            return "過重"
        elif BMI <= 30:
            return "輕度肥胖"
        elif BMI <=35:
            return "中度肥胖"
        else:
            return "重度肥胖"
    except (ValueError, TypeError):
        return "輸入錯誤"
