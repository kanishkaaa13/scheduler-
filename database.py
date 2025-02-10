import sqlite3
from datetime import datetime

def create_table():
    conn = sqlite3.connect('scheduler.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS posts
                 (id INTEGER PRIMARY KEY, content TEXT, platform TEXT, schedule_time TEXT, status TEXT)''')
    conn.commit()
    conn.close()

def save_post(content, platform, schedule_time):
    conn = sqlite3.connect('scheduler.db')
    c = conn.cursor()
    c.execute("INSERT INTO posts (content, platform, schedule_time, status) VALUES (?, ?, ?, ?)",
              (content, platform, schedule_time, "pending"))
    conn.commit()
    conn.close()

def get_scheduled_posts():
    conn = sqlite3.connect('scheduler.db')
    c = conn.cursor()
    c.execute("SELECT * FROM posts WHERE status = 'pending'")
    posts = c.fetchall()
    conn.close()
    return posts

def delete_post(post_id):
    conn = sqlite3.connect('scheduler.db')
    c = conn.cursor()
    c.execute("DELETE FROM posts WHERE id = ?", (post_id,))
    conn.commit()
    conn.close()

# Initialize database table
create_table()