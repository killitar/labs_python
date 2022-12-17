import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None

    try:
        connection = sqlite3.connect(path)
        print("Connection successful")
    except Error as e:
        print(f"The error'{e}' occurred")
    return connection


connection = create_connection("path to data base")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error'{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


create_movies_table = """
CREATE TABLE IF NOT EXISTS movies (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL UNIQUE, 
  year INTEGER NOT NULL,
  image_url VARCHAR(255) NOT NULL,
  runtime INT
  
);
"""
execute_query(connection, create_movies_table)


create_directors_table = """
CREATE TABLE IF NOT EXISTS directors(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  name VARCHAR(45) NOT NULL UNIQUE,
  about TEXT
);
"""

execute_query(connection, create_directors_table)

create_stars_table = """
CREATE TABLE IF NOT EXISTS stars(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  name VARCHAR(45) NOT NULL UNIQUE,
  about TEXT
);
"""
execute_query(connection, create_stars_table)


create_genres_table = """
CREATE TABLE IF NOT EXISTS genres(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  name VARCHAR(45) NOT NULL UNIQUE
);
"""
execute_query(connection, create_genres_table)


create_movies_directors_table = """
CREATE TABLE IF NOT EXISTS movies_directors(
  movies_id INTEGER NOT NULL ,
  directors_id INTEGER NOT NULL,
  FOREIGN KEY(movies_id) REFERENCES movies(id),
  FOREIGN KEY(directors_id) REFERENCES directors(id)
);
"""
execute_query(connection, create_movies_directors_table)


create_movies_stars_table = """
CREATE TABLE IF NOT EXISTS movies_directors(
  movies_id INTEGER NOT NULL ,
  stars_id INTEGER NOT NULL,
  FOREIGN KEY(movies_id) REFERENCES movies(id),
  FOREIGN KEY(stars_id) REFERENCES stars(id)
);
"""
execute_query(connection, create_movies_stars_table)


create_movies_genres_table = """
CREATE TABLE IF NOT EXISTS movies_directors(
  movies_id INTEGER NOT NULL , 
  genres_id INTEGER NOT NULL,
  FOREIGN KEY(movies_id) REFERENCES movies(id),
  FOREIGN KEY(genres_id) REFERENCES genres(id)
);
"""
execute_query(connection, create_movies_genres_table)


create_movies = """
INSERT INTO
  movies (title, year, image_url, runtime)
VALUES
  ('Harry Potter and the Philosophers Stone',2001, 'None', 152 ),
  ('Harry Potter and the Chamber of Secrets',2002, 'None', 161);
"""
execute_query(connection, create_movies)

create_directors = """
INSERT INTO
  directors (name,about)
VALUES
  ("Chris Columbus", "An American filmmaker. Born in Spangler, Pennsylvania, Columbus studied film at Tisch School of the Arts where he developed an interest in filmmaking.");

"""
execute_query(connection, create_directors)

create_stars = """
INSERT INTO
  stars (name,about)
VALUES
  ("Daniel Radcliffe","An English actor. He rose to fame at age twelve, when he began portraying Harry Potter in the film series of the same name.");

"""
execute_query(connection, create_stars)

create_genres = """
INSERT INTO
  genres (name)
VALUES
  ("Fantasy");

"""
execute_query(connection, create_genres)


select_movies = "SELECT * FROM movies"
movies = execute_read_query(connection, select_movies)
for movie in movies:
    print(movie)


select_directors = "SELECT * FROM directors"
directors = execute_read_query(connection, select_directors)
for director in directors:
    print(director)
