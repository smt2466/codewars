"""I Liked the SQL Better...
https://www.codewars.com/kata/53d2c97d7152a59b64001033

Create an SQLite3 database /tmp/movies.db

Your database should have a table named MOVIES that contains the following data:

    Name	                        Year	Rating
    Rise of the Planet of the Apes	2011	77
    Dawn of the Planet of the Apes	2014	91
    Alien	                        1979	97
    Aliens	                        1986	98
    Mad Max	                        1979	95
    Mad Max 2: The Road Warrior	    1981	100
"""

import os
import sqlite3

conn = sqlite3.connect(os.path.join('tmp', 'movies.db'))
cursor = conn.cursor()

cursor.execute('''CREATE TABLE MOVIES
                  (name TEXT, year INTEGER, rating INTEGER)''')

cursor.execute('''INSERT INTO movies VALUES
                  ('Rise of the Planet of the Apes', 2011, 77),
                  ('Dawn of the Planet of the Apes', 2014, 91),
                  ('Alien', 1979, 97),
                  ('Aliens', 1986, 98),
                  ('Mad Max', 1979, 95),
                  ('Mad Max 2: The Road Warrior', 1981, 100)''')

conn.commit()
conn.close()
