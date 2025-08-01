from flask import Flask, request, jsonify, render_template
import re
import os
import psycopg2
from dotenv import load_dotenv

app = Flask(__name__)

# 資料庫連線
load_dotenv()
conn = psycopg2.connect(
    host=os.getenv("PG_HOST"),
    port=os.getenv("PG_PORT"),
    user=os.getenv("PG_USER"),
    password=os.getenv("PG_PASSWORD"),
    dbname=os.getenv("PG_DB")
)
cursor = conn.cursor()

# 建立使用者表（若尚未存在）
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")
conn.commit()

# 驗證正規式
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
PWD_REGEX = r'^(?=.*[A-Z])(?=.*\d).{6,}$'

@app.route("/")
def index():
    return render_template("testweb.html")

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()

    if not re.match(EMAIL_REGEX, username):
        return jsonify({"error": "註冊失敗：Email 格式錯誤"}), 400
    if not re.match(PWD_REGEX, password):
        return jsonify({"error": "註冊失敗：密碼格式錯誤"}), 400

    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    if cursor.fetchone():
        return jsonify({"error": "帳號已存在"}), 409

    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    return jsonify({"message": "註冊成功"}), 200

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()

    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    if cursor.fetchone():
        return jsonify({"message": "登入成功"}), 200
    else:
        return jsonify({"error": "帳號或密碼錯誤"}), 401

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # 本地預設 5000，Render 用它指定的
    app.run(debug=True, host="0.0.0.0", port=port)