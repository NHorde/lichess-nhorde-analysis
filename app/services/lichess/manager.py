from services.lichess.request import request as request_lichess_api
from libs.state import State
from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)

def initialization(state: State):

    number_games = 5
    start_date = 5
    end_date = 5

    parameters = {
        "number_games": number_games,
        "start_date": start_date,
        "end_date": end_date
    }

    state.client.capture(variables=parameters)

    return request_lichess_api()

def manager():
    initialization(state=State())
