from libs.state import State
from libs.logger import BASE_LOGGER
import pandas as pd

from setup import ROOT_PATH
import os

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
    return pd.json_normalize(state.games[row])


def convert_to_dataframe(state: State):
    """
    Convert json in state.games into dataframe for further analysis
    :param state: state
    :type state: state
    :return: dataframe
    :rtype: state
    """
    LOGGER.info("Initializing parser")

    try:
        # Initialization
        state.df = parser(state=state, row=0)

        # Loop
        for i in range(len(state.games)-1):
            state.df = state.df.append(parser(state=state, row=i+1),
                           ignore_index=False)

        LOGGER.info("Successfully parsed json into dataframe")

    except Exception as e:
        LOGGER.error(f"Could not parse json: {e}")

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
        state.df.to_csv(ROOT_PATH + "/results/data.csv")
    except Exception as e:
        LOGGER.debug(f"Could not save dataframe file: {e}")

    LOGGER.info("Successfully saved dataframe in ../results")


def manager(state: State):
    convert_to_dataframe(state=state)

