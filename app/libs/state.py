from libs.models.client import Client
from libs.models.request import Request

class State:
    _defaults = {
        'status': 400
    }

    def __init__(self, **kwargs):
        """
        :param event:
        :type even: dict
        """
        self.games: Games = Games(**kwargs)
        self.request: Request = Request(**kwargs)

