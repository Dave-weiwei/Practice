USER_DB = {
    "admin@test.com": "admin123",
    "user1@example.com": "password1",
    "abc@aaaa": "password1"
}

def login_check(username, password):
    if not isinstance(username, str) or not isinstance(password, str):
        return "輸入格式錯誤"
    if "@" not in username or len(username) < 6:
        return "輸入格式錯誤"
    if len(password.strip()) < 8:
        return "輸入格式錯誤"
    if username not in USER_DB or USER_DB[username] != password:
        return "帳號或密碼錯誤"
    return "登入成功"