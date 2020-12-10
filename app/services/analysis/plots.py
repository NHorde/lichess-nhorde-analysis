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
        plt.figure(figsize=(15, 12))
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
        plt.xlabel("Month")
        plt.ylabel("# Games")

        plt.savefig(ROOT_PATH + "/results/graphs/model_1.png")

    except Exception as e:
        LOGGER.error(f"Plot 1 failed - Opening type - {e}")

    return plot_opening_diversity_2020(state=state)

def plot_opening_diversity_2020(state: State):
    """
    Plot opening diversity over the months

    :param state: state
    :type state: state
    :return: plot
    :rtype: plot
    """
    LOGGER.debug("Plotting game type over the months")

    try:
        df = state.games.df.loc[state.games.df["date_year"] == "2020"]

        plt.figure(figsize=(15, 12))
        chart = sns.countplot(
            data=df,
            x='opening.name.aggregate',
            hue='perf',
            order=df["opening.name.aggregate"].value_counts().iloc[:20].index
        )
        chart.set_xticklabels(chart.get_xticklabels(),
                              rotation=45,
                              horizontalalignment='right',
                              )
        chart.invert_xaxis()
        chart.set_title("Game type in 2020")
        plt.xlabel("Game ECO")
        plt.ylabel("# Games")

        plt.savefig(ROOT_PATH + "/results/graphs/model_2.png")

    except Exception as e:
        LOGGER.error(f"Plot 2 failed - Opening diversity - {e}")


def plot_models(state: State):
    plot_game_type(state=state)