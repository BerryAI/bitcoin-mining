#!/usr/bin/env python

import json
import logging
import urllib
import webapp2

from decorator import check_token
from decorator import log_required_params


from google.appengine.api import urlfetch

ONEMUSICAPI_BASE_HREF = "http://api.onemusicapi.com/20150623"
DUMMY_BASE_HREF = "http://lab.dj4.me/devices/CHANNEL0TEST02/recommendations/"


ONEMUSICAPI_USER_KEY = "40eed80da0001006b15ced17325d395f"



class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


# call
class FetchOneMusicApiHandler(webapp2.RequestHandler):
    @check_token
    @log_required_params("title", "artist")
    def get(self):

        self.response.headers["Content-Type"] = "application/json"

        title = self.request.get("title")
        artist = self.request.get("artist")

        form_fields = {
            "user_key": ONEMUSICAPI_USER_KEY,
            "title": title,
            "artist": artist,
        }
        form_data = urllib.urlencode(form_fields)

        url = ONEMUSICAPI_BASE_HREF + "/track"
        url = url + "?" + form_data

        try:

            logging.info("urlfetch call to " + url)

            result = urlfetch.fetch(
                url=url,
                payload=form_data,
                method=urlfetch.GET,
                headers={'Content-Type': 'application/x-www-form-urlencoded'}
            )

            logging.info("status_code = " + str(result.status_code))
            logging.info("result.content = (next line)")
            logging.info(result.content)

            self.response.headers["Content-Type"] = "application/json"
            self.response.write(result.content)

            # self.response.write("Done, see log")

        except:
            logging.info("error")
            self.response.write(json.dumps({"status": "error"}))


    def post(self):
        self.get()

#


class FetchDumpApiHandler(webapp2.RequestHandler):
    @check_token
    @log_required_params("title", "artist")
    def get(self):

        self.response.headers["Content-Type"] = "application/json"

        title = self.request.get("title")
        artist = self.request.get("artist")


        form_data = urllib.urlencode({
            "title": title,
            "artist": artist,
        })

        url = DUMMY_BASE_HREF

        try:
            result = urlfetch.fetch(
                url=url,
                payload=form_data,
                method=urlfetch.GET,
                headers={'Content-Type': 'application/x-www-form-urlencoded'}
            )

            logging.info(result.content)
            self.response.write(result.content)

        except:
            logging.info("error")
            self.response.write(json.dumps({"status": "error"}))

    def post(self):
        self.get()

#




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/onemusicapi/tracks', FetchOneMusicApiHandler),
    ('/dump/tracks', FetchDumpApiHandler),
], debug=True)
