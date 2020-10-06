from libs.state import State
from services.analysis.processing import clean_data
from services.analysis.plots import plot_models
from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)

def processing_data(state: State):
    """
    Processing and cleaning data function
    :param state: state
    :type state: state
    :return: state
    :rtype: state
    """
    LOGGER.debug("Starting data processing")

    try:
        clean_data(state=state)
        LOGGER.debug("Data processed with success")

    except Exception as e:
        LOGGER.error(f"Could not process raw date: {e}")

    return plot_graphs(state=state)


def plot_graphs(state: State):
    """
    Plotting graphs of Lichess games

    :param state: state
    :type state: state
    :return: state
    :rtype: state
    """

    LOGGER.debug("Plotting graphs")

    try:
        plot_models(state=state)
        LOGGER.debug("Plots created with success")
    except Exception as e:
        LOGGER.error(f"Could not plot graphs: {e}")

def manager(state: State):
    """
    Main function to call analysis service

    :param state: state
    :type state: state
    :return: state
    :rtype: state
    """
    processing_data(state=state)