from libs.state import State
from services.analysis.processing import clean_data
from services.analysis.plots import plot_models
from libs.logger import BASE_LOGGER

from setup import ROOT_PATH

import pandas as pd

LOGGER = BASE_LOGGER.getChild(__name__)

def read_data(state: State):
    """
    Reading data

    :param state: state
    :type state: state
    :return: state
    :rtype: state
    """
    LOGGER.debug("Reading data")

    try:
        state.games.df = pd.read_csv(ROOT_PATH + "/results/raw_data.csv")
        LOGGER.debug("Successfully read data")

    except Exception as e:
        LOGGER.error(f"Impossible to read data in /results/ - {e}")

    return processing_data(state=state)


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
        LOGGER.error(f"Could not process raw date - {e}")

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
        LOGGER.error(f"Could not plot graphs - {e}")


def manager(state: State):
    """
    Main function to call analysis service

    :param state: state
    :type state: state
    :return: state
    :rtype: state
    """
    read_data(state=state)