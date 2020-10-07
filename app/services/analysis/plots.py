from libs.state import State
from libs.logger import BASE_LOGGER

from setup import ROOT_PATH

import seaborn as sns
import matplotlib.pyplot as plt

LOGGER = BASE_LOGGER.getChild(__name__)

def plot_game_type(state: State):
    """
    Plot game type over the months

    :param state: state
    :type state: state
    :return: plot
    :rtype: plot
    """
    LOGGER.debug("Plotting game type over the months")

    try:
        plt.figure(figsize=(10, 5))
        chart = sns.countplot(
            data=state.games.df,
            x='date_year_month',
            hue='perf'
        )
        chart.set_xticklabels(chart.get_xticklabels(),
                              rotation=45,
                              horizontalalignment='right',
                              )
        chart.invert_xaxis()
        chart.set_title("Game type over the months")
        plt.xlabel("Months")
        plt.ylabel("# Games")

        plt.savefig(ROOT_PATH + "/results/model_1.png")

    except Exception as e:
        LOGGER.error(f"Plot 1 failed - Opening type - {e}")

    return plot_opening_diversity(state=state)

def plot_opening_diversity(state: State):
    """
    Plot opening diversity over the months

    :param state: state
    :type state: state
    :return: plot
    :rtype: plot
    """
    LOGGER.debug("Plotting game type over the months")

    try:
        plt.figure(figsize=(10, 5))
        chart = sns.countplot(
            data=state.games.df,
            x='opening.eco'
        )
        chart.set_xticklabels(chart.get_xticklabels(),
                              rotation=45,
                              horizontalalignment='right',
                              )
        chart.invert_xaxis()
        chart.set_title("Game diversity")
        plt.xlabel("Eco")
        plt.ylabel("# Games")

        plt.savefig(ROOT_PATH + "/results/model_2.png")

    except Exception as e:
        LOGGER.error(f"Plot 2 failed - Opening diversity - {e}")

def plot_models(state: State):
    plot_game_type(state=state)