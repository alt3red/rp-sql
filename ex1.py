import sqlite3

data = (
	('Ford', 'Taurus', 5),
	('Ford', 'Focus', 55),
	('Ford', 'Explorer', 8),
	('Honda', 'Civic', 3),
	('Honda', 'CRX', 2)
)

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()
	c.executemany("INSERT INTO inventory VALUES(?,?,?)", data)