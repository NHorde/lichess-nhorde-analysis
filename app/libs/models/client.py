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
        self.since = kwargs.get("since", "Account creation date")
        self.until = kwargs.get("until", "Now")
        self.max = kwargs.get("until", None)
        self.vs = kwargs.get("vs", None)

        self.rated = kwargs.get("rated", None)
        self.perf_type = kwargs.get("perf_type", None)
        self.color = kwargs.get("color", None)
        self.analyzed = kwargs.get("analyzed", None)
        self.ongoing = kwargs.get("ongoing", False)
        self.moves = kwargs.get("moves", True)

        self.pgn_json: int = kwargs.get("pgn_json", False)
        self.tags = kwargs.get("tags", True)
        self.clocks = kwargs.get("tags", False)

        self.evals: int = kwargs.get("evals", False)
        self.opening = kwargs.get("opening", False)
        self.players = kwargs.get("players", None)
