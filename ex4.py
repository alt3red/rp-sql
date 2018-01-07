import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("CREATE TABLE orders(make TEXT, model TEXT, order_date DATE)")

    data = [
        ('Ford', 'Taurus', '2014-11-06'),
        ('Ford', 'Taurus', '2014-10-06'),
        ('Ford', 'Taurus', '2014-09-06'),
        ('Ford', 'Focus', '2014-11-06'),
        ('Ford', 'Focus', '2014-10-06'),
        ('Ford', 'Focus', '2014-09-06'),
        ('Ford', 'Explorer', '2014-11-06'),
        ('Ford', 'Explorer', '2014-10-06'),
        ('Ford', 'Explorer', '2014-09-06'),
        ('Honda', 'Civic', '2014-11-06'),
        ('Honda', 'Civic', '2014-10-06'),
        ('Honda', 'Civic', '2014-09-06'),
        ('Honda', 'CRX', '2014-11-06'),
        ('Honda', 'CRX', '2014-10-06'),
        ('Honda', 'CRX', '2014-09-06'),
    ]

    c.executemany("INSERT INTO orders VALUES(?,?,?)", data)
