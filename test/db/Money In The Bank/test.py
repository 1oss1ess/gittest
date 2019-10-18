import psycopg2

print('asd')
conn = psycopg2.connect("dbname=bank")
cursor = conn.cursor()

