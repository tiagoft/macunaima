#import web
#from web.contrib.template import render_jinja

#import app.db.id3tosql
#rendier = render_jinja(
#         constants.template_directory,   # Set template directory.
#         encoding = 'utf-8',                         # Encoding.
#         )

class Insert():
    def __init__(self, render):
        self.render = render



    def GET(self, name):
#        artist = get_input.get('artist', default=None)
#        composer = get_input.get('artist', default=None)
#        album = get_input.get('album', default=None)
#        recording_date = get_input.get('regording_date', default=None)
#        location = get_input.get('location', default=None)
#        genre = get_input.get('genre', default=None)
#        url = get_input.get('url', default=None)
#        mp3_file = get_input.get('mp3_filename', default=None)
#        comments = get_input.get('comments', default=None)


        return self.render.add_new(property_list =\
                [ {'name': 'title', 'value': '', 'type': 'line'},
                  {'name': 'artist', 'value': '', 'type': 'line'},
                  {'name': 'album', 'value': '', 'type': 'line'},
                  {'name': 'composer', 'value': '', 'type': 'line'},
                  {'name': 'original_release_date', 'value': '',\
                          'type': 'line'},
                  {'name': 'recording_date', 'value': '', 'type': 'line'},
                  {'name': 'location', 'value': '', 'type': 'line'},
                  {'name': 'genre', 'value': '', 'type': 'line'},
                  {'name': 'url', 'value': '', 'type': 'line'},
                  {'name': 'comments', 'value': '', 'type': 'box'},
                  {'name': 'mp3_file', 'value': '', 'type': 'file'}])


