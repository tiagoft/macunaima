# Macunaima

curl -H "Content-Type: application/json" -X POST -d '{"username":"xyz","password":"xyz"}' http://localhost:3000/api/login

Content-Based Media Exploration

## API


### Get a new session ID
`curl -X GET http://localhost:8080/initialize`

### Inform the system that you like (or want to skip) a song
`curl -H "Content-Type: application/json" -X POST -d '{"session_id": "090b5ab14743bef753a219574135", "media_file": "static/audio/test1.mp3", "action": "skip"}' http://localhost:8080/recommend`

* Action must be either `like` or `skip`
* Session\_id is the session ID received when using initialize
* media\_file is the currently playing media file


