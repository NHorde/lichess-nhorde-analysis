from libs.state import State
from services.lichess.manage import manager as manager_lichess
from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)



def lichess_service(state: State):
    """
    Request sent to Lichess API
    :param state: state
    :type state: state
    :return: function
    :rtype: function
    """
    LOGGER.info("Attempting to run Lichess service")
    try:
        manager_lichess(state=state)
        LOGGER.info("Lichess service successfully run")

    except Exception as e:
        LOGGER.error(f"Lichess service manager failed: {e}")



def manager(state: State):
    lichess_service(state=state)


