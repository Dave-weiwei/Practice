import os
import psycopg2

# 資料庫連線設定
def get_connection():
    return psycopg2.connect(
        host=os.getenv("dpg-d1uu19mr433s73f4fkm0-a"),
        port=os.getenv("5432"),
        user=os.getenv("practice_dave"),
        password=os.getenv("jlbXz5pqIWztluSG6hsOKUMgTXuGny3K"),
        dbname=os.getenv("practice_db_ns14")
    )


def query_user(username):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT username FROM users WHERE username = %s", (username,))
        return cur.fetchone()
    finally:
        cur.close()
        conn.close()

def query_user_and_password(username, password):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT username, password FROM users WHERE username = %s AND password = %s", (username, password))
        return cur.fetchone()
    finally:
        cur.close()
        conn.close()

def insert_user(username, password):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
    finally:
        cur.close()
        conn.close()

def delete_user(username):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM users WHERE username = %s", (username,))
        conn.commit()
    finally:
        cur.close()
        conn.close()