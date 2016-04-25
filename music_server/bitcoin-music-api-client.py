#!/usr/bin/env python3

# Import methods from the 21 Bitcoin Library
from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests



import json


# Change this to the IP address of your 21 Bitcoin Computer.
# You can find this with `sudo hostname --ip-address`
SERVER_IP_ADDRESS = '127.0.0.1'

# Configure your Bitcoin wallet.
wallet = Wallet()
requests = BitTransferRequests(wallet)


# Send query to the endpoint
def send_query(*args):

    title = ""
    artist = ""

    count = 0

    for i in args[0]:
        # print(i)
        if count == 1:
            title = i
        if count == 2:
            artist = i

        count += 1


    if title == "" or artist == "":
        print("Error: Both title and artist cannot be both blank")
        return

    result_url = ('http://' + SERVER_IP_ADDRESS + ':6001/tracks?&title=' + title + '&artist=' + artist)

    print("result_url")
    print(result_url)
    results = requests.get(url=result_url)

    print("results.text")
    print(results.text)

    print('-------------------------------------------------')
    print(json.loads(results.text))



# Read the query to speechify from the CLI
if __name__ == '__main__':
    from sys import argv

    send_query(argv)

