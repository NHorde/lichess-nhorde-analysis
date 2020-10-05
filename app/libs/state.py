from libs.models.client_api import Client
from libs.models.games import Games

class State:
    _defaults = {
        'status': 400
    }

    def __init__(self, **kwargs):
        """
        :param event:
        :type even: dict
        """
        self.client: Client = Client(**kwargs)
        self.games: Games = Games(**kwargs)

