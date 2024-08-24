#!/usr/bin/env python

import logging
import sys
import os
import requests
import json
from pprint import pformat

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'setup')))

from config import config_credentials

def fetch_playlist_item_page(google_api_key, playlistId, page_token=None):
    response = requests.get("https://www.googleapis.com/youtube/v3/playlistItems",
        params={
            "key": google_api_key,
            "playlistId": playlistId,
            "part": "contentDetails",
            "pageToken": page_token
                            })
    # logging.info("GOT %s", pformat(json.loads(response.text)))
    return json.loads(response.text)

def fetch_video_items_page(google_api_key, video_id):
    response = requests.get("https://www.googleapis.com/youtube/v3/videos",
                            params={
                                "key": google_api_key,
                                "id": video_id,
                                "part": "snippet, statistics"
                            })
    logging.info("Got video details %s", pformat(json.loads(response.text)))

def fetch_playlist_item(google_api_key, playlistId, page_token=None):
    payload = fetch_playlist_item_page(google_api_key, playlistId, page_token)

    yield from payload["items"]

    next_page_token = payload.get("nextPageToken")
    if next_page_token is not None:
        yield from fetch_playlist_item(google_api_key, playlistId, next_page_token)

def main():
    logging.info("Started!")

    google_api_key = config_credentials["google_api_key"]
    playlistId = config_credentials["playlistId"]

    for video_item in fetch_playlist_item(google_api_key, playlistId):
        video_id = video_item['contentDetails']["videoId"]
        logging.info("Got videoId %s", video_id)
        fetch_video_items_page(google_api_key, video_id)
        break

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    sys.exit(main())    