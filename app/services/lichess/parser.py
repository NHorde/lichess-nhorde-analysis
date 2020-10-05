from libs.state import State
from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)

def parser(state: State):
    LOGGER.info("Initializing parser")
    # print(json.dumps(state.games[0], indent=3))
    # exit(1)
    # print(games[1].get("id"))

