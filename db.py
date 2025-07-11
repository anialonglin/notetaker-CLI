import os
from dotenv import load_dotenv
import psycopg2

# load_dotenv()  # this loads .env into os.environ
load_dotenv(dotenv_path="/Users/anialin/Desktop/codingExercise/notetaker-CLI/database_credentials.env")

# Connect to PostgreSQL
def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

def create_note(title, content):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO notes (title, content) VALUES (%s, %s)", (title, content))
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Note created.")

def list_notes():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, content FROM notes")
    rows = cur.fetchall()
    for row in rows:
        print(f"[{row[0]}] {row[1]}: {row[2]}")
    cur.close()
    conn.close()

def update_note(note_id, title=None, content=None):
    if not title and not content:
        print("⚠️ Please provide --title or --content to update.")
        return

    conn = get_connection()
    cur = conn.cursor()

    if title and content:
        cur.execute("UPDATE notes SET title = %s, content = %s WHERE id = %s", (title, content, note_id))
    elif title:
        cur.execute("UPDATE notes SET title = %s WHERE id = %s", (title, note_id))
    elif content:
        cur.execute("UPDATE notes SET content = %s WHERE id = %s", (content, note_id))

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Note updated.")

def delete_note(note_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM notes WHERE id = %s", (note_id,))
    conn.commit()
    cur.close()
    conn.close()
    print("🗑️ Note deleted.")
