# Jaci Brown || CSD 310 || MOD 8.2

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
    #input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or passowrd are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

#finally: 
#    db.close() 
# This was closing the connection even without error, moved to end and removed finally.


#Formatting
print()
print()
cursor = db.cursor()
def show_films(cursor, title):
    #method to execute an inner join on all tables, 
    #   iterate over the dataset and output the results 
    #   to the terminal window.

    #inner join query
    cursor.execute("""select film_name as Name, film_director as Director, 
                   genre_name as Genre, studio_name as 'Studio Name' 
                   from film INNER JOIN genre ON film.genre_id=genre.genre_id
                   INNER JOIN studio ON film.studio_id=studio.studio_id; """)
    
    #get the results from the cursor object
    films= cursor.fetchall()

    print("\n  -- {} --".format(title))
    print()
    #iterate over the film dataset and display the results. 
    for film in films: 
        print("""
                Film Name: {}\n
                Director: {}\n
                Genre Name ID: {}\n
                Studio Name: {}\n
                """.format(film[0], film[1], film[2], film[3]))

# #5, Display all films
show_films(cursor, "DISPLAYING FILMS")

# #6, Insert a new record

insertMyMovie ="""INSERT INTO film (film_name, film_releaseDate, film_runtime, 
film_director, studio_id, genre_id) 
VALUES('Meet The Parents', 2000, 108, 'Jay Roach', 3, 3 );"""
cursor.execute(insertMyMovie)

# #7, Demonstrate insertion
show_films(cursor, "-- DISPLAYING FILMS AFTER INSERT --")


# #8, Update Alien to Horror
updateAlien = """UPDATE film
                SET genre_id= 1
                WHERE film_name = 'Alien' AND film_id= '2';"""
cursor.execute(updateAlien) 

# #9- Demonstrate Update
show_films(cursor, "-- DISPLAYING FILMS -- Update Alien to Horror --")

# #10, Delete Gladiator
deleteGladiator = """ DELETE FROM film WHERE film_id = 1"""
cursor.execute(deleteGladiator)

# #11, Demonstrate Deletion
show_films(cursor, "-- DISPLAYING FILMS -- Delete Gladiator --")




