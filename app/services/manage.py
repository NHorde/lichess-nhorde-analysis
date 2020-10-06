from libs.state import State
from services.lichess.manage import manager as manager_lichess
from services.analysis.manage import manager as manager_analysis
from libs.logger import BASE_LOGGER

from inflection import underscore
LOGGER = BASE_LOGGER.getChild(__name__)


def lichess_service(state: State):
    """
    Request sent to Lichess API

    :param state: state
    :type state: state
    :return: function
    :rtype: function
    """

    LOGGER.debug("Attempting to run Lichess service")

    try:
        manager_lichess(state=state)
        LOGGER.info("Lichess service successfully run")

    except Exception as e:
        LOGGER.error(f"Lichess service manager failed: {e}")

    return analysis_service(state=state)


def analysis_service(state: State):
    """
    Analysis of lichess games
    :param state: state
    :type state: state
    :return: state
    :rtype: state
    """

    LOGGER.debug("Attempting to analyze Lichess games")

    try:
        manager_analysis(state=state)
        LOGGER.info("Analysis of Lichess games successfully completed")

    except Exception as e:
        LOGGER.error(f"Analysis of Lichess games failed: {e}")


def manager(state: State):
    """
    Master manager

    :param state: state
    :type state: state
    :return: state
    :rtype: state
    """
    LOGGER.debug("Master manager initialization")

    if underscore(state.environment) == "plot":
        LOGGER.info("Bypassing API, read archive data file")
        analysis_service(state=state)

    else:
        LOGGER.debug("Full script called")
        lichess_service(state=state)



