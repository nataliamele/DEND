# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("CREATE TABLE IF NOT EXISTS songplay (\
                        songplay_id SERIAL PRIMARY KEY, \
                        start_time TIMESTAMP, \
                        user_id INT, \
                        level VARCHAR, \
                        song_id VARCHAR(50), \
                        artist_id  VARCHAR(50), \
                        session_id INT, \
                        location VARCHAR, \
                        user_agent TEXT \
                        );") 

#Dimensions tables:

user_table_create = ("CREATE TABLE IF NOT EXISTS users (\
                    user_id INT PRIMARY KEY, \
                    first_name VARCHAR, \
                    last_name VARCHAR, \
                    gender VARCHAR(3), \
                    level VARCHAR \
                    );")

song_table_create = ("CREATE TABLE IF NOT EXISTS songs( \
                    song_id VARCHAR(50) PRIMARY KEY, \
                    title VARCHAR(255), \
                    artist_id VARCHAR(50), \
                    year INT, \
                    duration DOUBLE PRECISION) \
                    ;")

artist_table_create = ("CREATE TABLE IF NOT EXISTS artist( \
                    artist_id VARCHAR PRIMARY KEY, \
                    name VARCHAR(127), \
                    location VARCHAR(255), \
                    lattitude FLOAT, \
                    longitude FLOAT);")

time_table_create = ("CREATE TABLE IF NOT EXISTS time(\
                    start_time TIMESTAMP, \
                    hour INT, \
                    day INT, \
                    week INT, \
                    month INT, \
                    year INT, \
                    weekday INT)\
                    ;")
#1541106106796


# INSERT RECORDS

songplay_table_insert = ("INSERT INTO songplay( \
                    start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

user_table_insert = ("INSERT INTO users(user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s) \
                    ON CONFLICT (user_id) DO NOTHING")

song_table_insert = ("INSERT INTO songs(song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s) \
                    ON CONFLICT (song_id) DO NOTHING;")

artist_table_insert = ("INSERT INTO artist(artist_id, name, location, lattitude, longitude) \
                    VALUES (%s, %s, %s, %s, %s) \
                    ON CONFLICT (artist_id) DO NOTHING;") 

time_table_insert = ("INSERT INTO time(start_time, hour, day, week, month, year, weekday) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s)")

# FIND SONGS

song_select = ("SELECT songs.song_id, artist.artist_id \
                FROM songs JOIN artist on songs.artist_id=artist.artist_id \
                WHERE songs.title=(%s) AND artist.name=(%s) AND songs.duration=(%s)"
                )


# SONG PLAY ANALYSIS

## How many songs matched : 


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]