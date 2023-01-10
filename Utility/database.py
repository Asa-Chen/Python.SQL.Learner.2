import sqlite3
from datetime import datetime
CREATE_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    title,
    release_date,
    watched)"""
MARK_MOVIE = "UPDATE movies SET watched=? WHERE title=?"
INSERT_MOVIES = "INSERT INTO movies (title, release_date, watched) VALUES (?, ?, 0)"
DELETE_MOVIES = "DELETE FROM movies WHERE title=?"
SELECT_ALL_MOVIES = "SELECT * FROM movies"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_date > ?"

connection = sqlite3.connect('data.db')

def create_table():
    with connection:
        connection.execute(CREATE_TABLE)

def add_movie(title, release_date):
    with connection:
        connection.execute(INSERT_MOVIES, (title, release_date,))

def delete_movie(title):
    with connection:
        connection.execute(DELETE_MOVIES, (title,))

def select_movies():
    with connection:
        return connection.execute(SELECT_ALL_MOVIES).fetchall()

def mark_movie(title):
    with connection:
        connection.execute(MARK_MOVIE, (1, title))

def check_presense(title):
    with connection: #bool of a list returned by a cursor.fetchall() from connection
        return bool(connection.execute("SELECT * FROM movies WHERE title=?", (title,)).fetchall())

