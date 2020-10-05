from libs.state import State
from services.lichess.manage import manager as manager_lichess
from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)

def get_lichess_response(state: State):
    try:
        manager_lichess(state=state)
    except Except as e:
        LOGGER.error(f"Lichess API manager failed: {e}")



def manager(state: State):
    get_lichess_response(state=state)


