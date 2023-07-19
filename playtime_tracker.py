#!/usr/bin/env python
import os
import sys

import requests

try:
    STEAM_API_KEY = os.environ["STEAM_KEY"]
    STEAMID = os.environ["STEAM_ID"]
    API_URL = os.environ["API_URL"]
    API_USERNAME = os.environ["API_USERNAME"]
    API_PASSWORD = os.environ["API_PASSWORD"]
except KeyError:
    sys.stderr.write(
        "Supply environment variables STEAM_API_KEY, STEAMID, "
        "API_URL, API_USERNAME, API_PASSWORD\n"
    )
    sys.exit(1)

response = requests.get(
    "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/",
    params={
        "key": STEAM_API_KEY,
        "steamid": STEAMID,
        "include_appinfo": True,
        "include_played_free_games": True,
        "appids_filter": [],
        "include_free_sub": True,
        "language": "en",
        "include_extended_appinfo": True,
    },
    timeout=60,
)
response.raise_for_status()

total_playtime = {"windows": 0, "mac": 0, "linux": 0}
for game in response.json()["response"]["games"]:
    for platform in total_playtime:
        total_playtime[platform] += game[f"playtime_{platform}_forever"]

response = requests.post(
    API_URL,
    auth=(API_USERNAME, API_PASSWORD),
    data=total_playtime,
    timeout=60,
)
response.raise_for_status()
