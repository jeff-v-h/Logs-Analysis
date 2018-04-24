import psycopg2

def get_popular_articles():
	db = psycopg2.connect("dbname=news")
	cursor = db.cursor()
	cursor.execute("SELECT * from articles")
	results = cursor.fetchall()
	print results
	db.close()

get_popular_articles()