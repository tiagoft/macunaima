import web
import sqlite3

import constants

from web.contrib.template import render_jinja

render = render_jinja(
         constants.mypath + "/" + constants.template_directory,   # Set template directory.
         encoding = 'utf-8',                         # Encoding.
         )

class Media():
    def __init__(self):
        self.gen_id = None

    def GET(self):
        return render.media_player()


        #return #[(i, get_input[i]) for i in get_input]

    def POST(self):
        get_input = web.input(_method='post')

        title = get_input.get('title')
        artist = get_input.get('artist')
        composer = get_input.get('composer')
        album = get_input.get('album')
        recording_date = get_input.get('recording_date')
        original_release_date = get_input.get('original_release_date')
        location = get_input.get('location')
        genre = get_input.get('genre')
        url = get_input.get('url')
        mp3_file = web.input(mp3_file={})
        comments = get_input.get('comments')

        try:
            recording_date = str(int(unicode(recording_date)))
        except:
            recording_date = "0"

        try:
            original_release_date = str(int(unicode(original_release_date)))
        except:
            original_release_date = "0"

        mp3_filename = web.input(mp3_file={}).mp3_file.filename


        query = "INSERT INTO media (title, artist, album, recording_date, "+\
          "original_release_date, genre, file, user, link, comments, composer)"+\
                            "VALUES ('" +\
                            unicode(title) + "', '" +\
                            unicode(artist) + "', '" +\
                            unicode(album) + "', " +\
                            unicode(recording_date) + ", " +\
                            unicode(original_release_date) + ", '" +\
                            unicode(genre) + "', '" +\
                            unicode(mp3_filename) + "', '" +\
                            "admin', '" +\
                            unicode(url) + "', '" + \
                            unicode(comments) + "', '" +\
                            unicode(composer) + "');".decode('unicode_escape')


        conn = sqlite3.connect(constants.dbfile)
        c = conn.cursor()
        c.execute(query)
        conn.commit()

        if mp3_filename is not '':
            gen_tag = c.lastrowid
            filename = str(gen_tag) + "_" + mp3_filename
            fout = open(constants.files_directory +'/'+ filename,'w')
            fout.write(web.input(mp3_file={}).mp3_file.file.read())
            fout.close()

        return web.seeother('/hello')
        #return "OK"
