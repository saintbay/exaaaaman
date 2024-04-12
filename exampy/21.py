import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS cinema (id INTEGER PRIMARY KEY, name TEXT, address TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS movie (id INTEGER PRIMARY KEY, name TEXT, genre TEXT, year INTEGER,  description TEXT, rating REAL)')
    cursor.execute('CREATE TABLE IF NOT EXISTS afisha (id INTEGER PRIMARY KEY, movie_id INTEGER, cinema_id INTEGER, price INTEGER, date DATE, time TIME, capacity INTEGER)')
    cursor.execute('CREATE TABLE IF NOT EXISTS place (id INTEGER PRIMARY KEY, afisha_id INTEGER, room INTEGER, row INTEGER, seat INTEGER)')
    cursor.execute('CREATE TABLE IF NOT EXISTS ticket (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, place_id INTEGER)')
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,name TEXT,card_number TEXT,password_hash TEXT)')
create_table()