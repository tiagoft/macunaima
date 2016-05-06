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

        return self.render.information_table(property_list = [ {'name': 'Title', 'value': '', 'type': 'line'},
                                                                {'name': 'Artist', 'value': 'No one', 'type': 'box'},
                                                                {'name': 'File', 'value': 'file.mp3', 'type': 'file'}])


