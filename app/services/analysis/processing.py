from libs.state import State
from libs.logger import BASE_LOGGER

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
        LOGGER.debug("Columns successfully coverted to lower cases")

    except Exception as e:
        LOGGER.error(f"Columns not converted to lower case: {e}")

    return convert_date(state=state)

def convert_date(state: State):
    """
    Add extra columns to handle dates more efficiently

    :param state: state
    :type state: state
    :return: state
    :rtype: state
    """





def clean_data(state: State):
    """
    Getting and processing data

    :param state: state
    :type state: state
    :return: state
    :rtype: state
    """
    lower_columns(state=state)