# Python2

import psycopg2

# Connect to the news sql database with postgresql
db = psycopg2.connect("dbname=news")
cursor = db.cursor()

# Execute a query to fetch and print the 3 most popular articles of all time
cursor.execute(
    "SELECT title, count(*) as views from articles, log \
    where log.path like CONCAT('%', articles.slug, '%') \
    and (status = '200 OK') group by title \
    order by views desc limit 3")
results = cursor.fetchall()
print "1. What are the most popular three articles of all time?"
for result in results:
    print result[0] + " - " + str(result[1]) + " views"

# Execute a query to fetch and print the authors ordered by most views
cursor.execute(
    "SELECT name, count(*) as views from articles, authors, log \
    where log.path like CONCAT('%', articles.slug, '%') \
    and articles.author = authors.id group by name \
    order by views desc")
results = cursor.fetchall()
print "2. Who are the most popular article authors of all time?"
for result in results:
    print result[0] + " - " + str(result[1]) + " views"

# Execute a query to fetch and print days with more than 1% of request errors
cursor.execute("SELECT * from authors")
results = cursor.fetchall()
# print results

# Close the database
db.close()
