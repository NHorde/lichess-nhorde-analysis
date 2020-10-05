from libs.logger import BASE_LOGGER
from inflection import underscore

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

        if not isinstance(value, int):
            LOGGER.error(f"Start date is not an integer: {value}")
        else:
            start_date = int(value)
        self._start_date = start_date

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
        if not isinstance(value, int):
            LOGGER.error(f"End date is not an integer: {value}")
        else:
            end_date = int(value)
        self._end_date = end_date

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
        if not isinstance(value, int):
            LOGGER.error(f"Number of games is not an integer: {value}")
        else:
            number_games = int(value)
        self._number_games = number_games


    @property
    def color(self):
        """
        :rtype:  int
        """
        return self._color

    @color.setter
    def color(self, value):
        """
        :param value:
        :type value: int
        """
        if value not in ("black", "white"):
            LOGGER.error(f"Color must be 'black' or 'white': {value}")
        else:
            color = underscore(value)
        self._color = color

    @property
    def analyzed(self):
        """
        :return: binary
        :rtype: bool
        """
        return self._evals

    @analyzed.setter
    def analyzed(self, value):
        """
        :param value: bool
        :type value: bool
        :return: bool
        :rtype: bool
        """
        if not type(value) == bool:
            LOGGER.error(f"Evaluation must be a boolean: {value}")
        self._analyzed = value


    @property
    def opening(self):
        """
        :return:
        :rtype:
        """
        return self._opening

    @opening.setter
    def opening(self, value):
        """
        :param value: bool
        :type value: bool
        :return: bool
        :rtype: bool
        """
        if not type(value) == bool:
            LOGGER.error(f"Opening choice must be a boolean: {value}")
        self._opening = value