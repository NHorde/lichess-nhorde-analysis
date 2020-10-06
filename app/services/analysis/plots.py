from libs.state import State
from libs.logger import BASE_LOGGER

import seaborn as sns
import matplotlib.pyplot as plt

LOGGER = BASE_LOGGER.getChild(__name__)

def plot_opening_diversity(state: State):
    """
    Plot openings over the months

    :param state: state
    :type state: state
    :return: plot
    :rtype: plot
    """

    plt.figure(figsize=(10, 5))
    chart = sns.countplot(
        data=state.games.df,
        x='date_year_month'
    )
    chart.set_xticklabels(chart.get_xticklabels()
                          , rotation=45
                          , horizontalalignment='right')
    chart.invert_xaxis()
    plt.show()

    # sns.displot(state.games.df, x="date_year_month")
    #
    # plt.show()


def plot_models(state: State):
    plot_opening_diversity(state=state)