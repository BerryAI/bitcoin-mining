#!usrbinenv python3


# Import methods from the 21 Bitcoin Library
from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

# Change this to the IP address of your 21 Bitcoin Computer.
# You can find this with `sudo hostname --ip-address`
SERVER_IP_ADDRESS = '127.0.0.1'

# Configure your Bitcoin wallet.
wallet = Wallet()
requests = BitTransferRequests(wallet)


# Send query to the endpoint
def send_query(query):
    # tell the user what query they're sending
    print('You sent {0}'.format(query))

    # 402-payable endpoint URL and request
    tts_url = 'http://' + SERVER_IP_ADDRESS + ':7000/music?query={0}'
    speech = requests.get(url=tts_url.format(query))

    # save the received audio file to disk
    speech_output = open('speech.wav', 'wb')
    speech_output.write(speech.content)
    speech_output.close()

# Read the query to speechify from the CLI
if __name__ == '__main__':
    from sys import argv
    send_query(argv[1])
