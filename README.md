<h4>Project 1</h4>
<h1>Data Modeling with Postgres</h1>

<h3>Summary of the project</h3>

In this project we performed analyses for startup Sparkify to understand what songs users are listening to.

Sprakify shared 3 types of JSON log files, which contain information on user activity, songs, artists data.

To acomplish this task we model STAR schema in Postgres DB and implement ETL pipeline to fetch data from logs.

<h3>Fact Table </h3>

**songplays** - records in log data associated with song plays:
* songplay_id 
* start_time 
* user_id
* level
* song_id 
* artist_id 
* session_id
* location 
* user_agent

<h3>Dimension Tables</h3>

**users** - users in the app:
* user_id 
* first_name 
* last_name 
* gender 
* level

**songs** - songs in music database:
* song_id
* title
* artist_id 
* year
* duration

**artists** - artists in music database:
* artist_id 
* name 
* location 
* lattitude 
* longitude

**time** - timestamps of records in songplays broken down into specific units
* start_time 
* hour 
* day 
* week 
* month 
* year 
* weekday

<h3>How to run</h3>
To run project localy you need PostgreSQL and Python installed. You can find appropriate package and installation guides here:

- <a href="https://www.postgresql.org/download/">Postgres</a>
- <a href="https://www.anaconda.com/distribution/">Anaconda for Python</a>

We also going to need two libraries installed for our script - **Pandas** (to be able to read JSON file into dataframe object and perform operations on it) and **Psycopg** (to interract with database).

To instal Pandas , run in Terminal:
> conda install pandas

To install Psycopg2:
> pip install psycopg2

After instalation completed, you need to create default data base "studentdb", user "student", password "student" to be able to establish connection to Postgres.

You can find following scripts in the directory :
  
* etl.ipynb (Jupyter notebook file with sample ETL process)
* etl.py (script which runs ETL, processing log files and transporting data to database)
* sql_queries.py (contains SQL queries to create tables, insert and select data to tables)
* create_tables.py (contains drop and create tables queries)


Also there is a directory **\data** which contains all log files in JSON format

<h3>Steps to run project and gather stats:</h3> 

1. In the Terminal(command line) run command: 
> python create_tables.py 
This will create Sparkify database and Fact and all Dimensions tables. 
2. In the Terminal(command line) run command: 
> python etl.py
This will run ETL process, printing out details on processed log files. 
3. Now you have you data organized in tables and you can query for different stats. Connecto to database from terminal with command: 
> psql -d sparkifydb -U student

For example, if you want to display 20 most active 'paid' users, run this query:
> SELECT user_id, count(user_id) requests FROM songplay WHERE level = 'paid' GROUP BY user_id ORDER BY requests DESC LIMIT 20;

If you need information what browsers are most popular, run this query:
> SELECT user_agent, count(user_agent) FROM songplay GROUP BY user_agent ORDER BY count(user_agent) DESC;

