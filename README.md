Bitcoin Mining
================

Source code of projects relating to 21.co bitcoin computer

## Components

- Source code to be executed at 21.co machine
- Source code to be used at Google App Engine


## Software requirement

### 21.co Machine
- Python 3.4

### Google App Engine
- Python 2.7
- Google App Engine SDK


## Development

### Google App Engine - Local Environment

Refer to source code located at `aivvy-bitcoin-backend` directory, which is the GAE Application ID.

Execute following command to start server:

`python "C:\Program Files (x86)\Google\google_appengine\dev_appserver.py" ./ --port=8081 --log_level=debug --admin_port=9081` OR execute `start_server.sh`

Optionally change the server port and admin port if there is any conflict to your local settings. More options available here:  https://cloud.google.com/appengine/docs/python/tools/devserver.


## Deployment

### Auto run is enabled

NOTE: this step should not be required. There is already a script setup to run at system boot.

`sudo vi /etc/init.d/start_server.sh`

`sudo chmod 755 /etc/init.d/start_server.sh`

`python3 /home/twenty/music_server/bitcoin-music-api-server.py &`

### To deploy to 21.co Machine (If the process is killed, need to do this)

ssh to 21.co Machine (`twenty@192.168.0.103` @ office network)(DHCP)

Go to music_server directory
`cd ~/music_server`

Execute script, start server, run in background
`python3 bitcoin-music-api-server.py &`


### To deploy to Google App Engine

Deploy with Google App Engine Launcher, or follow the steps here: https://cloud.google.com/appengine/docs/python/gettingstartedpython27/uploading

You must have permission to update the app to deploy to Google App Engine.
