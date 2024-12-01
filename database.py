import sqlite3

def saveSurvey(name, phone, category, topic, language):
    conn = sqlite3.connect('survey.sqlite3')
    conn.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        category TEXT NOT NULL,
        topic TEXT,
        language TEXT
    );
    ''')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (name, phone, category, topic, language)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, phone, category, topic, language))
    conn.commit()
    conn.close()
