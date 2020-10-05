from libs.state import State
from services.lichess.manage import manager as manager_lichess
from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)

def manager(state: State):
    manager_lichess(state=state)


