import csv
import sqlite3

def populate_with_csv(csv_file_path, query):
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        cur.executemany(query, csv_reader)

def populate_users(conn, cur, sqlite_db_path):
    csv_file_path = './data/users_data.csv'

    cur.execute('''DROP TABLE IF EXISTS users''')
    columns=['user_id', 'username', 'email', 'aboutme', 'account_type', 'followers']

    cur.execute('''
    CREATE TABLE users (
        user_id TEXT,
        username TEXT,
        email TEXT,
        aboutme TEXT,
        account_type TEXT,
        followers INTEGER
    )
    ''')
    insert_query = 'INSERT INTO users (user_id, username, email, aboutme, account_type, followers) VALUES (?, ?, ?, ?, ?, ?)'
    populate_with_csv(csv_file_path, insert_query)

def populate_posts(conn, cur, sqlite_db_path):
    csv_file_path = './data/post_data.csv'

    cur.execute('''DROP TABLE IF EXISTS posts''')
    columns=['post_id', 'user_id', 'content', 'date']

    cur.execute('''
    CREATE TABLE posts (
        post_id TEXT,
        user_id TEXT,
        content TEXT,
        date TEXT
    )
    ''')
    insert_query = 'INSERT INTO posts (post_id, user_id, content, date) VALUES (?, ?, ?, ?)'
    populate_with_csv(csv_file_path, insert_query)

def populate_comments(conn, cur, sqlite_db_path):
    csv_file_path = './data/comments_data.csv'

    cur.execute('''DROP TABLE IF EXISTS comments''')
    columns=['comment_id', 'user_id', 'post_id', 'content', 'date']

    cur.execute('''
    CREATE TABLE comments (
        comment_id TEXT,
        user_id TEXT,
        post_id TEXT,
        content TEXT,
        date TEXT
    )
    ''')
    insert_query = 'INSERT INTO comments (comment_id, user_id, post_id, content, date) VALUES (?, ?, ?, ?, ?)'
    populate_with_csv(csv_file_path, insert_query)

def populate_likes(conn, cur, sqlite_db_path):
    csv_file_path = './data/likes_data.csv'

    cur.execute('''DROP TABLE IF EXISTS likes''')
    columns=['like_id', 'user_id', 'comment_id', 'post_id', 'date']

    cur.execute('''
    CREATE TABLE likes (
        like_id TEXT,
        user_id TEXT,
        comment_id TEXT,
        post_id TEXT,
        date TEXT
    )
    ''')
    insert_query = 'INSERT INTO likes (like_id, user_id, comment_id, post_id, date) VALUES (?, ?, ?, ?, ?)'
    populate_with_csv(csv_file_path, insert_query)

def populate_hashtags(conn, cur, sqlite_db_path):
    csv_file_path = './data/hashtags_data.csv'

    cur.execute('''DROP TABLE IF EXISTS hashtags''')
    columns=['hashtag_id', 'comment_id', 'post_id', 'hashtag_name']

    cur.execute('''
    CREATE TABLE hashtags (
        hashtag_id TEXT,
        comment_id TEXT,
        post_id TEXT,
        hashtag_name TEXT
    )
    ''')
    insert_query = 'INSERT INTO hashtags (hashtag_id, comment_id, post_id, hashtag_name) VALUES (?, ?, ?, ?)'
    populate_with_csv(csv_file_path, insert_query)

sqlite_db_path = './database.db'
conn = sqlite3.connect(sqlite_db_path)
cur = conn.cursor()

populate_users(conn, cur, sqlite_db_path)
populate_posts(conn, cur, sqlite_db_path)
populate_comments(conn, cur, sqlite_db_path)
populate_likes(conn, cur, sqlite_db_path)
populate_hashtags(conn, cur, sqlite_db_path)

conn.commit()
conn.close()

print("Data imported successfully.")