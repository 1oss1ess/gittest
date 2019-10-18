import psycopg2

conn = psycopg2.connect("dbname=bank")
cursor = conn.cursor()
print('test')
