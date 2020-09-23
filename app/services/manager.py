from libs.state import State
from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)

import requests
import os
import json

def manager():
    url = "https://www.lichess.org/api/games/user/nhorde"

    headers = {
        "accept":"application/x-ndjson"
        }

    params = {
        "max": 2,
        "perfType": "rapid",
        "analysed": "false",
        "clocks": "false",
        "evals": "false",
        "opening":"true"
        }

    r = requests.get(url,
                     params=params,
                     headers=headers)

    r_text = r.content.decode("utf-8")

    games = [json.loads(s) for s in r_text.split("\n")[:-1]]
    print(json.dumps(games[0], indent=3))

