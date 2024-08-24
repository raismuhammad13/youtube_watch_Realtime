#!/usr/bin/env python

import logging
import sys
import os
import requests
import json
from pprint import pformat

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'setup')))

from config import config_credentials

def fetch_playlist_item_page(google_api_key, playlistId):
    response = requests.get("https://www.googleapis.com/youtube/v3/playlistItems",
        params={
            "key": google_api_key,
            "playlistId": playlistId
            # "part": "contentDetails"
                            })
    logging.info("GOT %s", pformat(json.loads(response.text)))
    return json.loads(response.text)

def main():
    logging.info("Started!")

    google_api_key = config_credentials["google_api_key"]
    playlistId = config_credentials["playlistId"]

    fetch_playlist_item_page(google_api_key, playlistId)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    sys.exit(main())    