# Jaci Brown || CSD 310 || MOD 7.2

import mysql.connector
from mysql.connector import errorcode

config = {
"user": "movies_user",
"password": "popcorn",
"host": "127.0.0.1",
"database": "movies",
"raise_on_warnings": True

}

try:
    db= mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with databse {} ".format(config["user"], config ["host"], config ["database"]))
    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or passowrd are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

#finally: 
#    db.close() 
# This was closing the connection even without error


#ADDING SPACING FROM CONNECTION
print()
print()
# Query 1: All fields in studio table
    
cursor = db.cursor()
showStudioRecords = "SELECT * FROM studio;"
cursor.execute(showStudioRecords)
studios = cursor.fetchall()
print(' -- DISPLAYING Studio RECORDS -- ')
for studio in studios:
    print("Studio ID: {}\n Studio Name: {}\n" .format(studio[0], studio[1] )) #-- two fields

print()
print()

# Query 2: All fields in Genre table
showGenreRecords = "SELECT * FROM genre;"
cursor.execute(showGenreRecords)
genres = cursor.fetchall()
print(" -- DISPLAYING Genre RECORDS --")
for genre in genres:
    print(" Genre ID: {}\n Genre Name: {}\n" .format(genre[0], genre[1] ))

print()
print()

# Query 3: Show movies shorter than 2 hours.
moviesUnder120 = " SELECT film_name, film_runtime FROM film WHERE film_runtime <= 120;"
cursor.execute(moviesUnder120)
shortFilms = cursor.fetchall()
print(" -- DISPLAYING Short Film RECORDS -- ")
for movie in shortFilms:
    print("Film Name: {} \nRuntime: {}\n" .format(movie[0], movie[1]))

print()
print()

# Query 4: 
filmsByDirector = " SELECT film_director, film_name FROM film ORDER BY film_director;"
cursor.execute(filmsByDirector)
filmList = cursor.fetchall()
print(" -- DISPLAYING Director RECORDS in Order -- ")
for film in filmList:
    print("Film Name: {} \nDirector {}\n" .format(film[0], film[1]))


db.close() 