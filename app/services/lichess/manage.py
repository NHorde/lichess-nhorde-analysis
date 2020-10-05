from services.lichess.request import request as request_lichess_api
from libs.state import State
from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)

def get_lichess_request(state: State):
    request_lichess_api(state=state)

def manager(state: State):
    get_lichess_request(state=state)
