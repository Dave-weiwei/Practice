def register_user(email, password):
    try:
        if not isinstance(email, str) or not isinstance(password, str):
            return "輸入格式錯誤"
        if "@" not in email or email.startswith("@") or email.endswith("@") or len(email) < 6:
            return "輸入格式錯誤"
        if len(password.strip()) < 6 or password.isalpha() or password.isdigit():
            return "輸入格式錯誤"
        
        return "註冊成功"
    except Exception as e:
        print("錯誤內容：", e)