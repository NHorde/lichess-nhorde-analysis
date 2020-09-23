from libs.state import State
from services.lichess.manager import manager as manager_lichess
from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)

def manager():
    manager_lichess()


