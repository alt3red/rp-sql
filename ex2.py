import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("UPDATE inventory SET Quantity=6 WHERE Make='Ford' AND Model='Taurus'")
	c.execute("UPDATE inventory SET Quantity=5 WHERE Make='Honda' AND Model='Civic'")

	c.execute("SELECT * FROM inventory")

	print("\nNew Data\n")

	rows = c.fetchall()

	for r in rows:
		print(r[0], r[1], r[2])