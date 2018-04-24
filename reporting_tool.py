# Python2

import psycopg2

# Connect to the news sql database with postgresql
db = psycopg2.connect("dbname=news")
cursor = db.cursor()

# Execute a query to fetch and print the 3 most popular articles of all time
cursor.execute("SELECT * from articles")
results = cursor.fetchall()
print results

# Execute a query to fetch and print the authors ordered by most views
cursor.execute("SELECT * from authors")
results = cursor.fetchall()
print results

# Execute a query to fetch and print the days with more than 1% of request errors
cursor.execute("SELECT * from authors")
results = cursor.fetchall()
print results

# Close the database
db.close()


'''
# Query news database to fetch and print three most popular articles of all time 
def get_popular_articles():
	db = psycopg2.connect("dbname=news")
	cursor = db.cursor()
	cursor.execute("SELECT * from articles")
	results = cursor.fetchall()
	print results
	db.close()

# Query news db to fetch and print most popular article authors of all time
def get_popular_authors():
	db = psycopg2.connect("dbname=news")
	cursor = db.cursor()
	cursor.execute("SELECT * from authors")
	results = cursor.fetchall()
	print results
	db.close()

# Query news db to fetch and print days with errors in more than 1% of requests
def get_error_days():
	db = psycopg2.connect("dbname=news")
	cursor = db.cursor()
	cursor.execute("SELECT * from log")
	results = cursor.fetchall()
	print results
	db.close()

# get_popular_articles()
# get_popular_authors()
# get_error_days()'''