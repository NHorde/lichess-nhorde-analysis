from libs.state import State
from libs.logger import BASE_LOGGER

from setup import ROOT_PATH

from datetime import datetime

LOGGER = BASE_LOGGER.getChild(__name__)

def lower_columns(state: State):
    """
    Get everything lower case

    :param state: state
    :type state: state
    :return: state
    :rtype: state
    """
    LOGGER.debug("Appending year and month to dataframe")

    try:
        state.games.df.columns = map(str.lower, state.games.df.columns)
        state.games.df["index"] = 1
        LOGGER.debug("Columns successfully converted to lower cases")

    except Exception as e:
        LOGGER.error(f"Columns not converted to lower case - {e}")

    return convert_date(state=state)

def convert_date(state: State):
    """
    Add extra columns to handle dates more efficiently

    :param state: state
    :type state: state
    :return: state
    :rtype: state
    """
    LOGGER.debug("Converting unix epoch time into human readable date")

    try:
        # Get epoch time in seconds
        state.games.df["createdat_sec"] = state.games.df['createdat'] / 1000
        # Processing date
        state.games.df['date_complete'] = state.games.df["createdat_sec"].apply(lambda x: datetime.fromtimestamp(x).strftime("%Y-%m-%d"))
        state.games.df['date_year_month'] = state.games.df["createdat_sec"].apply(lambda x: datetime.fromtimestamp(x).strftime("%Y-%m"))

    except Exception as e:
        LOGGER.error(f"Could not convert time - {e}")

    return save_processed_data(state=state)


def save_processed_data(state: State):
    """
    Saving processed data next to raw data for further checks

    :param state: state
    :type state: state
    :return: state
    :rtype: state
    """
    LOGGER.debug("Saving processed data")

    try:
        state.games.df.to_csv(ROOT_PATH + "/results/processed_data.csv")
        LOGGER.debug("Successfully saved dataframe in ../results")

    except Exception as e:
        LOGGER.error(f"Could not save dataframe file - {e}")

def clean_data(state: State):
    """
    Getting and processing data

    :param state: state
    :type state: state
    :return: state
    :rtype: state
    """
    lower_columns(state=state)