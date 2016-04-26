#!/usr/bin/env python3
# from subprocess import call
# from uuid import uuid4

from flask import Flask
from flask import request
# from flask import send_from_directory

# Import from the 21 Bitcoin Developer Library
from two1.wallet import Wallet
from two1.bitserv.flask import Payment


import json
# import logging
import sys
import yaml


try:
    # python 3
    import urllib.request as urllib2
    from urllib.parse import urlencode
except ImportError:
    # python 2.7
    import urllib2
    from urllib import urlencode




# Configure the app and wallet
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)


# REQUEST_API_BASE_HREF = "http://aivvy-bitcoin-backend.appspot.com/dump"
REQUEST_API_BASE_HREF = "http://aivvy-bitcoin-backend.appspot.com/onemusicapi"



@app.route('/free')
def test():
    return "hello world"



@app.route('/tracks')
@payment.required(3000)  # Charge a fixed fee per request
def tracks():
    # the name the client sent us
    title = str(request.args.get('title', ""))
    artist = str(request.args.get('artist', ""))
    print("title = " + title)
    print("artist = " + artist)

    if title == "" or artist == "":
        print("Error: Both title and artist cannot be blank")
        return json.dumps({"status": "error", "error_detail": "title and artist cannot be blank"})


    data = {
        "token": "MpsI0PUj3ScKnn5cwUAiecUZ3wZ36kRi4ItxU3fD",
        "title": title,
        "artist": artist,
    }


    request_url = REQUEST_API_BASE_HREF + "/tracks" + "?" + urlencode(data)

    try:
        print("request url = " + request_url)
        result = urllib2.urlopen(request_url)  # , data=str(data))

        print_result = result.read()
        print(print_result)

    except urllib2.HTTPError as e:
        if hasattr(e, 'reason'):
            print ('We failed to reach a server.')
            print ('Reason: ' + e.reason)
        elif hasattr(e, 'code'):
            print ('The server couldn\'t fulfill the request.')
            print ('Error code: ' + e.code)

        print("HTTPError")
        print_result = json.dumps({"status": "error", "error_detail": "HTTPError"})

    except ValueError as e:
        print("ValueError")
        print_result = json.dumps({"status": "error", "error_detail": "ValueError"})

    except:
        print("Uncaught Error")
        e = sys.exc_info()[0]
        print(e)
        print_result = json.dumps({"status": "error", "error_detail": "Exception"})



    return print_result



@app.route('/manifest')
def manifest():
    '''
    Serves the app manifest to the 21 crawler.
    '''
    with open('manifest.yaml', 'r') as f:
        manifest_yaml = yaml.load(f)
    return json.dumps(manifest_yaml)



# Initialize and run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6002)  # MUSIC
