from datetime import datetime
import Utility.database as DBConnect
PROMPT = """Welcome to the movie watching app:
Add - Add new movie
Upcoming - View upcoming movies
All - View all movies
Mark - Mark watched movie
Watched - View watched movies
User - Add user to the app
Exit - Exit the app
Your choice: 
"""

def add_movie():
    title = input("Movie title: ")
    if DBConnect.check_presense(title):
        print("Movie already exists.")
    else:
        release_date = input("Release date as DD-MM-YYYY: ")
        release_date = datetime.strptime(release_date, "%d-%m-%Y")
        timestamp = release_date.timestamp()
        DBConnect.add_movie(title, timestamp)

def print_movies():
    movie_list = DBConnect.select_movies()
    for movie in movie_list:
        date = datetime.fromtimestamp(movie[1])
        date = date.date()
        print(f"{movie[0]} was released {date}")
        if movie[2]:
            print("You have watched this movie.")
        else:
            print("You have not watched this movie.")

def mark_movie():
    title = input("Movie to mark: ")
    if DBConnect.check_presense(title):
        DBConnect.mark_movie(title)
    else:
        print("Movie does not exists.")

def delete_movie():
    title = input("Movie to delete: ")
    if DBConnect.check_presense(title):
        DBConnect.delete_movie(title)
    else:
        print("Movie is not in list.")


def menu():
    DBConnect.create_table()
    while (choice := input(PROMPT)).lower() != 'end':
        if choice == 'add':
            add_movie()
        elif choice == 'upcoming':
            pass
        elif choice == 'all':
            print_movies()
        elif choice == 'mark':
            mark_movie()
        elif choice == 'watched':
            pass
        elif choice == 'user':
            pass
        elif choice == 'exit':
            return
        else:
            print("Invalid input.")

menu()