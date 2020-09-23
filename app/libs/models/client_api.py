from libs.logger import BASE_LOGGER

LOGGER = BASE_LOGGER.getChild(__name__)


class Client:
    def __init__(self, **kwargs):
        """
        :param kwargs:
        :type kwargs:
        """
        # API
        self.status: int = kwargs.get("status", 400)
        self.result: str = kwargs.get("result")

        # Parameters
        self._start_date = kwargs.get("start_date", None)
        self._end_date = kwargs.get("end_date", None)
        self._number_games = kwargs.get("number_games", None)
        self._vs = kwargs.get("vs", None)

        self._rated = kwargs.get("rated", None)
        self._perf_type = kwargs.get("perf_type", None)
        self._color = kwargs.get("color", None)
        self._analyzed = kwargs.get("analyzed", None)
        self._ongoing = kwargs.get("ongoing", False)
        self._moves = kwargs.get("moves", True)

        self._pgn_json: int = kwargs.get("pgn_json", False)
        self._tags = kwargs.get("tags", True)
        self._clocks = kwargs.get("tags", False)

        self._evals: int = kwargs.get("evals", False)
        self._opening = kwargs.get("opening", False)
        self._players = kwargs.get("players", None)


    # <~> Actions <~>

    def capture(self, variables: dict):
        """
        :param variables:
        :type variables: dict
        :rtype: Client
        """
        for k, v in variables.items():
            k = underscore(k)

            if hasattr(self, k) and v is not None:
                setattr(self, k, v)
        return self


    # <~> Properties <~>

    @property
    def start_date(self):
        """
        :rtype:  int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        """
        :param value:
        :type value: int
        """
        if not value.isnumeric():
            LOGGER.error(f"Start date is not an integer: {value}")
        self._start_date

    @property
    def end_date(self):
        """
        :rtype:  int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        """
        :param value:
        :type value: int
        """
        if not value.isnumeric():
            LOGGER.error(f"End date is not an integer: {value}")
        self._end_date

    @property
    def number_games(self):
        """
        :rtype:  int
        """
        return self._number_games

    @number_games.setter
    def number_games(self, value):
        """
        :param value:
        :type value: int
        """
        if not value.isnumeric():
            LOGGER.error(f"Number of games is not an integer: {value}")
        self._number_games