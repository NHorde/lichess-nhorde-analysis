import setup
from libs.state import State
from services.manage import manager as manager_services
from libs.logger import BASE_LOGGER

import os
from dotenv import load_dotenv
load_dotenv()

LOGGER = BASE_LOGGER.getChild(__name__)

def invoke(state: State):
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
    state.parameters = parameters
    state.username = os.getenv("USERNAME")

    return capture(state = state)

def capture(state):
    """
    :param state: state
    :type state: state
    :param parameters: dict
    :type parameters: dict
    :return: function
    :rtype: function
    """
    try:
        state.client.capture(variables=state.parameters)
        LOGGER.info("Parameters correctly initialized")

    except Exception as e:
        LOGGER.debug(f"Incorrect parameters, please check .env: {e}")

    return manager_services(state=state)


if __name__ == "__main__":
    invoke(state=State())