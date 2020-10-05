from libs.state import State
from libs.logger import BASE_LOGGER
import pandas as pd

LOGGER = BASE_LOGGER.getChild(__name__)

def parser(state: State):
    LOGGER.info("Initializing parser")

    df = pd.json_normalize(state.games[0])
    print(df)
    df.to_csv("test.csv")

    # print(games[1].get("id"))

