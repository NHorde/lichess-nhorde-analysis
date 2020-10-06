from libs.state import State
from libs.logger import BASE_LOGGER
import pandas as pd

from setup import ROOT_PATH

LOGGER = BASE_LOGGER.getChild(__name__)

def parser(state: State, row):
    """
    :param state: state
    :type state: state
    :param row: index row
    :type row: integer
    :return: dataframe
    :rtype: dataframe
    """
    return pd.json_normalize(state.games.response[row])


def convert_to_dataframe(state: State):
    """
    Convert json in state.games into dataframe for further analysis
    :param state: state
    :type state: state
    :return: dataframe
    :rtype: state
    """
    LOGGER.debug("Initializing parser")

    try:
        # Initialization
        state.games.df = parser(state=state, row=0)

        # Loop
        for i in range(len(state.games.response)-1):
            state.games.df = state.games.df.append(parser(state=state, row=i+1),
                           ignore_index=False)

        LOGGER.debug("Successfully parsed json into dataframe")

    except Exception as e:
        LOGGER.error(f"Could not parse json - {e}")

    return save_dataframe(state=state)


def save_dataframe(state: State):
    """
    Saving dataframe to save copy

    :param state: state
    :type state: state
    :return: state
    :rtype: state
    """

    try:
        state.games.df.to_csv(ROOT_PATH + "/results/raw_data.csv")
        LOGGER.debug("Successfully saved dataframe in ../results")

    except Exception as e:
        LOGGER.error(f"Could not save dataframe file - {e}")




def manager(state: State):
    convert_to_dataframe(state=state)

