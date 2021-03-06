import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    sql = {'Focus count': "SELECT count(make) FROM orders WHERE model = 'Focus'",
           'Taurus count': "SELECT count(make) FROM orders WHERE model = 'Taurus'",
           'Explorer count': "SELECT count(make) FROM orders WHERE model = 'Explorer'",
           'Civic count': "SELECT count(make) FROM orders WHERE model = 'Civic'",
           'CRX count': "SELECT count(make) FROM orders WHERE model = 'CRX'", } 

    for keys, values in sql.items():
        c.execute(values)
        result = c.fetchone()
        print(keys + ": ", result[0])
