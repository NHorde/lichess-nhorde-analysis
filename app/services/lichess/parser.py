from libs.state import State
from libs.logger import BASE_LOGGER
import pandas as pd

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
    LOGGER.info("Initializing parser")

    df = parser(state=state, row=0)

    for i in range(len(state.games)-1):
        df = df.append(parser(state=state, row=i+1),
                       ignore_index=False)

    df.to_csv("test.csv")


def manager(state: State):
    convert_to_dataframe(state=state)

