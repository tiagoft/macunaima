# This script initializes tables



import sqlite3
import os

import constants

# Check if DB directory exists
if not os.path.exists(constants.dbdir):
    os.makedirs(constants.dbdir)

conn = sqlite3.connect(constants.dbfile)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS media
                     (id int PRIMARY KEY,
                     title text,
                     artist text,
                     album text,
                     recording_date int,
                     original_release_date int,
                     genre text,
                     comments text,
                     link text,
                     user text,
                     file text)''')

c.execute('''CREATE TABLE IF NOT EXISTS features
                     (id int PRIMARY KEY,
                     media_id int,
                     algorithm text,
                     metadata text,
                     value text)''')

c.execute('''CREATE TABLE IF NOT EXISTS users
                    (username text PRIMARY KEY,
                    password text)''')

conn.commit()


for table in ['media', 'features', 'users']:
    results = c.execute('''SELECT * FROM ''' + table)
    print "TABLE", table, "has", len(list(results)), "lines"

