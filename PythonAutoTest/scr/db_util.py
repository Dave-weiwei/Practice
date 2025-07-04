import pymysql

# 資料庫連線設定
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "ok88468ok",  # 改成你自己的 MySQL 密碼
    "database": "test",
    "charset": "utf8mb4"
}

def query_user(username):
    """
    只查詢 username 是否存在。
    回傳 (username,) 或 None
    """
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    try:
        sql = "SELECT username FROM users WHERE username = %s"
        cursor.execute(sql, (username,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()


def query_user_and_password(username, password):
    """
    查詢 username + password 是否完全符合。
    回傳 (username, password) 或 None
    """
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    try:
        sql = "SELECT username, password FROM users WHERE username = %s AND password = %s"
        cursor.execute(sql, (username, password))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()


def delete_user(username):
    """
    刪除指定 username 的使用者（測試後清理用）
    """
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM users WHERE username = %s"
        cursor.execute(sql, (username,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()