import sqlite3

conn = sqlite3.connect('events.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE buy(
           id INTEGER PRIMARY KEY ASC, 
           buy_id VARCHAR(250) NOT NULL,
           item_name VARCHAR(250) NOT NULL,
           item_price FLOAT NOT NULL,
           buy_qty INTEGER NOT NULL,
           date_created VARCHAR(100) NOT NULL)
          ''')

c.execute('''
          CREATE TABLE sell(
           id INTEGER PRIMARY KEY ASC, 
           sell_id VARCHAR(250) NOT NULL,
           item_name VARCHAR(250) NOT NULL,
           item_price FLOAT NOT NULL,
           sell_qty INTEGER NOT NULL,
           date_created VARCHAR(100) NOT NULL)
          ''')

conn.commit()
conn.close()