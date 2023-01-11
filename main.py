from datetime import datetime
import Utility.database as DBConnect
PROMPT = """Welcome to the movie watching app:
Add - Add new movie
Upcoming - View upcoming movies*
All - View all movies
Mark - Mark watched movie
Watched - View watched movies
User - Add user to the app
Exit - Exit the app
Your choice: 
"""

def add_movie():
    title = input("Movie title: ").lower()
    if DBConnect.check_presense(title):
        print("Movie already exists.")
    else:
        release_date = input("Release date as DD-MM-YYYY: ")
        release_date = datetime.strptime(release_date, "%d-%m-%Y")
        timestamp = release_date.timestamp()
        DBConnect.add_movie(title, timestamp)

def add_user():
    user = input("Select a user to input: ").lower()
    DBConnect.add_user(user)

def print_all_movies():
    movie_list = DBConnect.select_movies()
    for movie in movie_list:
        date = datetime.fromtimestamp(movie[2])
        date = date.strftime("%d-%m-%Y")
        print(f"{movie[0]}: {movie[1]} released {date}\n")

def print_watched_movies():
    user = input("User to search for: ").lower()
    watched_list = DBConnect.select_watched(user)
    for movie in watched_list:
        print(f"\n{movie[0]} has watched this movie id: {movie[1]}")

def mark_movie():
    id = input("Movie ID: ").lower()
    if DBConnect.check_movie_presense(id):
        user = input("Who watched the movie? (user): ").lower()
        DBConnect.mark_movie(user, id)
    else:
        print("Movie does not exists.")

def delete_movie(): #Needs work
    title = input("Movie to delete: ").lower()
    if DBConnect.check_movie_presense(title):
        DBConnect.delete_movie(title)
    else:
        print("Movie is not in list.")


def menu():
    DBConnect.create_table()
    while (choice := input(PROMPT)).lower() != 'exit':
        if choice == 'add':
            add_movie()
        elif choice == 'upcoming':
            pass
        elif choice == 'all':
            print_all_movies()
        elif choice == 'mark':
            mark_movie()
        elif choice == 'watched':
            print_watched_movies()
        elif choice == 'user':
            add_user()
        else:
            print("Invalid input.")

menu()