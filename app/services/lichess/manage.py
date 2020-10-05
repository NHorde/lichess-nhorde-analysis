from services.lichess.request import request as request_lichess_api
from services.lichess.parser import parser as parse_lichess_response

from libs.state import State
from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)

def get_lichess_request(state: State):
    """
    Request Lichess API

    :param state: state
    :type state: state
    :return: function
    :rtype: function
    """
    LOGGER.info("Attempting to call Lichess API")

    try:
        request_lichess_api(state=state)
        LOGGER.info("Lichess API successfully called")

    except Exception as e:
        LOGGER.error(f"Lichess API request failed: {e}")
    return convert_lichess_response(state=state)


def convert_lichess_response(state: State):
    """
    Parse lichess API info pandas dataframes

    :param state: state
    :type state: state
    :return:function
    :rtype: function
    """

    LOGGER.info("Attempting to parse Lichess API response")

    try:
        parse_lichess_response(state=state)
        LOGGER.info("Lichess response successfully converts into dataframe")

    except Exception as e:
        LOGGER.error(f"Parsing Lichess request failed: {e}")



def manager(state: State):
    get_lichess_request(state=state)
