import requests
import json

from libs.state import State
from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)


def request():
    state = State()
    number_games = 5
    start_date = 5
    end_date = 5
    parameters = {
        "number_games": 1,
        "start_date": 1,
        "end_date": 1
    }

    state.client.capture(variables=parameters)
    exit(1)
    url = "https://www.lichess.org/api/games/user/nhorde"

    headers = {
        "accept": "application/x-ndjson"
    }

    params = {
        "max": 2,
        "perfType": "rapid",
        "analysed": "false",
        "clocks": "false",
        "evals": "false",
        "opening": "true"
    }

    r = requests.get(url,
                     params=params,
                     headers=headers)

    r_text = r.content.decode("utf-8")

    games = [json.loads(s) for s in r_text.split("\n")[:-1]]
    #     print(json.dumps(games[1], indent=3))
    print(games[1].get("id"))
    LOGGER.info("Good")
