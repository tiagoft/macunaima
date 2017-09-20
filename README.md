# Macunaima

curl -H "Content-Type: application/json" -X POST -d '{"username":"xyz","password":"xyz"}' http://localhost:3000/api/login

Content-Based Media Exploration

## API


### Get a new session ID
curl -X GET http://localhost:8080/initialize

### Inform the system that you like a song
curl -X GET http://localhost:8080/recommend/action/session-id/media-file

* Action must be either `like` or `skip`
* Session-id is the session ID received when using initialize
* media-file is the currently playing media file



