
import eyed3
import sqlite3
import os



def id3tosql(mp3_filename, dbfile):
    metadata = eyed3.load(mp3_filename).tag

    if metadata.genre.id == 255:
        genre = "None"
    else:
        genre = metadata.genre.name

    if metadata.original_release_date is None:
        original_release_date = 0
    else:
        original_release_date = metadata.original_release_date

    if metadata.recording_date is None:
        recording_date = 0
    else:
        recording_date = metadata.recording_date

    #print metadata.title
    #print metadata.artist
    #print metadata.album
    #print metadata.recording_date
    #print metadata.original_release_date
    #print genre
    #print mp3_filename

    query = "INSERT INTO media (title, artist, album, recording_date, "+\
                "original_release_date, genre, file, user) VALUES ('" +\
                            unicode(metadata.title) + "', '" +\
                            unicode(metadata.artist) + "', '" +\
                            unicode(metadata.album) + "', " +\
                            unicode(recording_date) + ", " +\
                            unicode(original_release_date) + ", '" +\
                            genre + "', '" +\
                            mp3_filename + "', '" +\
                            "admin');"
    #print query


    conn = sqlite3.connect(dbfile)
    c = conn.cursor()
    c.execute(query)
    conn.commit()





if __name__ == "__main__":
    import sys
    print sys.argv[1]
    print sys.argv[2]
    id3tosql(sys.argv[1], sys.argv[2])

