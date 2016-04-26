Bitcoin Mining
================

Source code of projects relating to 21.co bitcoin computer

## Components

- Source code to be executed at 21.co machine
- Source code to be used at Google App Engine


## Software requirement

### 21.co Machine
- Python 3.4
- `screen` is installed by  `sudo apt-get install screen`

### Google App Engine
- Python 2.7
- Google App Engine Python SDK


## Development

### Google App Engine - Local Environment

Refer to source code located at `aivvy-bitcoin-backend` directory, which is the GAE Application ID.

Execute following command to start server:

`python "C:\Program Files (x86)\Google\google_appengine\dev_appserver.py" ./ --port=8081 --log_level=debug --admin_port=9081` OR execute `start_server.sh`

Optionally change the server port and admin port if there is any conflict to your local settings. More options available here:  https://cloud.google.com/appengine/docs/python/tools/devserver.


## Deployment

### Auto run is enabled

NOTE: this step should not be required. There is already a script setup to run at system boot.


```
touch /etc/init.d/start_server.sh
sudo chmod 755 /etc/init.d/start_server.sh
```

Inside `/etc/init.d/start_server.sh`, there is a script calling screen

```bash
#!/bin/bash
/usr/bin/screen -S server /home/twenty/music_server/start-server.sh
```

Inside `~/music_server/start-server.sh`,
```bash
python3 /home/twenty/music_server/bitcoin-music-api-server.py &
```


### To deploy to 21.co Machine (If the process is killed, need to do this)

`ssh` to 21.co Machine (`twenty@192.168.0.103` @ office network)(DHCP)

Go to music_server directory
`cd ~/music_server`

Execute script, start server, run in background
`python3 bitcoin-music-api-server.py &`


### To deploy to Google App Engine

Deploy with Google App Engine Launcher, or follow the steps here: https://cloud.google.com/appengine/docs/python/gettingstartedpython27/uploading

You must have permission to update the app to deploy to Google App Engine.


## Check the request log

Google App Engine acts as the middle man handling the requests sent from 21.co computer to API service providers.

Visit https://appengine.google.com/logs?app_id=s~aivvy-bitcoin-backend to view the traffic between these servers.
