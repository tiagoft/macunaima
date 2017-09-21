# Macunaima

Content-Based Media Exploration Server

## Running and basic configuration

This program is written in Python, using the web.py framework. The main file is
`src/web-app.py`. Hence, you can run a local recommendation server by going to
the `src` directory and typing:

`python web-app.py`

The program will automatically create some folders, which are specified in the
`config.yaml` file (relative to the application's root directory):

* `data/audio`: all audio files in the database should be copied or linked here
* `data/user`: user and session database files will be created here.
* `data/metadata`: data about audio files (e.g., datasets with audio
  descriptors) will be created here.

You can choose to change the directories by changing the `config.yaml` file.

A link in `src/static/audio` will also be created. It will point to
`data/audio`. This will facilitate access to audio files in the recommendation
process.

## API
This API description assumes you are running the Macunaima server locally. If
you deploy the system to a webserver, please remember to change all references
to `http://localhost:8080` to your server's address.

### First, get a new session ID
When a new session begins, the client must request a new session ID from the
server. This happens with a `GET` requeste to the `initialize` resource:

`curl -X GET http://localhost:8080/initialize`

The server will reply with a JSON string like this:

`{"timestamp": 1505994340.150185, "response": "init", "session_id":
"9450591cad464554bb7d642228de3eda", "recommendation": "static/audio/test1.mp3"}`

The "recommendation" property is a link to the recommended file. The session ID
is a unique identifier for the session, and must be kept by the client and used
in all communications.

### Inform the system that you like (or want to skip) a song
The client can inform the server that a user likes or wants to skip a song. This
is done using a `POST` request to the `recommend`. The request must send JSON data
regarding the request:

`curl -H "Content-Type: application/json" -X POST -d '{"session_id": "9450591cad464554bb7d642228de3eda", "media_file": "static/audio/test1.mp3", "action": "skip"}' http://localhost:8080/recommend`

* Action must be either `like` or `skip`
* Session\_id is the session ID received when using initialize
* media\_file is the currently playing media file

The server will reply with a JSON string like this:

`{"timestamp": 1505994604.524167, "response": "recommend", "session_id":
"9450591cad464554bb7d642228de3eda", "recommendation": "static/audio/test2.mp3"}`

It is the same string as in the `initialize` resource, but the response is
`recommend` instead of `init`. This allows the client to keep track of all
server recommendations.

