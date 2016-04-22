# This script initializes tables



import sqlite3
import os

import constants

# Check if DB directory exists
if not os.path.exists(constants.dbdir):
    os.makedirs(constants.dbdir)

conn = sqlite3.connect(constants.dbfile)
c = conn.cursor()
c.execute('''CREATE TABLE media
                     (id int,
                     title text,
                     comments text,
                     link text,
                     file text)''')
conn.commit()



