from libs.models.client_api import Client
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
        self.client: Client = Client(**kwargs)
        self.request: Request = Request(**kwargs)

