from libs.state import State
from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)

def clean_data(state: State):
    """
    Getting and processing data

    :param state: state
    :type state: state
    :return: state
    :rtype: state
    """
    print(state.games.df)
    return