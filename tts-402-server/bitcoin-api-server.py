#!/usr/bin/env python3
from subprocess import call
from uuid import uuid4

from flask import Flask
from flask import request
from flask import send_from_directory

# Import from the 21 Bitcoin Developer Library
from two1.wallet import Wallet
from two1.bitserv.flask import Payment


import json
import yaml


# Configure the app and wallet
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)


# Charge a fixed fee of 1000 satoshis per request to the
# /music endpoint
@app.route('/music')
@payment.required(1000)
def music():
    # the query the client sent us
    query = str(request.args.get('query'))

    # a file to store the rendered audio file
    file = str(uuid4()) + '.wav'

    # run the TTS engine
    call(['espeak', '-w', '/tmp/' + file, query])

    # send the rendered audio back to the client
    return send_from_directory(
        '/tmp',
        file,
        as_attachment=True
    )


@app.route('/manifest')
def docs():
    '''
    Serves the app manifest to the 21 crawler.
    '''
    with open('manifest.yaml', 'r') as f:
        manifest_yaml = yaml.load(f)
    return json.dumps(manifest_yaml)


# Initialize and run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
