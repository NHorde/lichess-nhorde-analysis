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
    # df = sns.load_dataset()
    # sns.displot(state.games.df, x="flipper_length_mm")

    sns.displot(state.games.df, x="date_month")

    plt.show()


def plot_models(state: State):
    plot_opening_diversity(state=state)