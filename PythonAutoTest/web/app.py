from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ok88468ok",  # ← 改成你自己的密碼
    database="testsite"
)
cursor = conn.cursor()

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data["username"]
    password = data["password"]
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        return jsonify({"message": "註冊成功"})
    except mysql.connector.Error as e:
        return jsonify({"error": str(e)}), 400

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data["username"]
    password = data["password"]
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()
    if result:
        return jsonify({"message": "登入成功"})
    else:
        return jsonify({"message": "登入失敗"}), 401

if __name__ == "__main__":
    app.run(debug=True)