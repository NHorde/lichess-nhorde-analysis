from libs.state import State

import requests
import json

from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)


def request(state: State):

    url = "https://www.lichess.org/api/games/user/" + state.username

    headers = {
        "accept": "application/x-ndjson"
    }

    params = state.parameters

    r = requests.get(url = url,
                     params=params,
                     headers=headers)

    r_text = r.content.decode("utf-8")

    games = [json.loads(s) for s in r_text.split("\n")[:-1]]
    #     print(json.dumps(games[1], indent=3))
    # print(games[1].get("id"))
    LOGGER.info("Good")
