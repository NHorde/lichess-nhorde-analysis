from services.lichess.request import request as request_lichess_api
from libs.state import State
from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)

def initialization(state: State):
    """
    Initialize parameters and make sure that correct type is provided

    :param state: state
    :type state: state
    :return: function
    :rtype: function
    """


    number_games = 5
    start_date = 5
    end_date = 5
    color = "white"
    evals = False

    parameters = {
        "number_games": number_games,
        "start_date": start_date,
        "end_date": end_date,
        "color": color,
        "evals": evals
    }

    state.client.capture(variables=parameters)
    LOGGER.info("Parameters correctly initialized")
    return request_lichess_api()

def manager():
    LOGGER.info("Beginning of script")
    initialization(state=State())
