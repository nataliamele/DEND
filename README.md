<h4>Project 1</h4>
<h1>Data Modeling with Postgres</h1>

<h3>Summary of the project</h3>
<p>In this project we performed analyses for startup Sparkify to understand what songs users are listening to.</p>

<p>Sprakify shared 3 types of JSON log files, which contain information on user activity, songs, artists data. </p>
To acomplish this task we had to model STAR schema in Postgres DB and implement ETL pipeline to fetch data from logs.</p>

<h3>How to run</h3>
<p>To run project localy you need PostgreSQL and Python installed. You can find appropriate package and installation guides here: </p>
- <a href="https://www.postgresql.org/download/">Postgres</a>
- <a href=""https://www.python.org/downloads/>Python</a>
<p>After instalation completed, you need to create default data base "studentdb", user "student", password "student:to be able to establish connection to Postgres. </p>

<p>You can find several scripts in the directory :
-etl.ipynb (Jupyter notebook file with sample ETL process)
-etl.py (script which runs ETL, processing log files and transporting data to database)
-sql_queries.py (contains SQL queries to create tables, insert and select data to tables)
-create_tables.py (contains drop and create tables queries)
</p>

Steps: 
1. In terminal(command line) run: <b> python create_tables.py </b>. This will create Sparkify database and tables. 
2. In terminal run <b> python etl.py </b>. This will run ETL process, printing out details on processed log files. 
3. Now you have you data organized in tables and you can query for different stats. Connecto to database from terminal with command: <b>psql -d sparkifydb -U student</b>