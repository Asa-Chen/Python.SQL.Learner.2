import sqlite3
from datetime import datetime
CREATE_MOVIE_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    title,
    release_date)"""
CREATE_WATCHED_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    watcher, 
    title)"""
MARK_MOVIE = "UPDATE movies SET watched=? WHERE title=?"
INSERT_MOVIES = "INSERT INTO movies (title, release_date) VALUES (?, ?)"
INSERT_WATCHED = "INSERT INTO watched (watcher, title) VALUES (?, ?)"
DELETE_WATCHED = "DELETE FROM watched WHERE title=?"
DELETE_MOVIES = "DELETE FROM movies WHERE title=?"
SELECT_ALL_MOVIES = "SELECT * FROM movies"
SELECT_WATCHED = "SELECT * FROM watched WHERE watcher=?"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_date > ?"
SELECT_WATCHED_MOVIES = "SELECT * FROM watched WHERE watcher = ?"

connection = sqlite3.connect('data.db')

def create_table():
    with connection:
        connection.execute(CREATE_MOVIE_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)

def add_movie(title, release_date):
    with connection:
        connection.execute(INSERT_MOVIES, (title, release_date,))

def delete_movie(title):
    with connection:
        connection.execute(DELETE_MOVIES, (title,))

def select_movies(): #returns a list of tuples
    with connection:
        return connection.execute(SELECT_ALL_MOVIES).fetchall()

def select_watched(user): #returns a list of tuples
    with connection:
        return connection.execute(SELECT_WATCHED, (user,)).fetchall()

def mark_movie(user, title):
    with connection:
        connection.execute(DELETE_MOVIES, (title,))
        connection.execute(INSERT_WATCHED, (user, title,))

def check_presense(title):
    with connection: #bool of a list returned by a cursor.fetchall() from connection
        return bool(connection.execute("SELECT * FROM movies WHERE title=?", (title,)).fetchall())

