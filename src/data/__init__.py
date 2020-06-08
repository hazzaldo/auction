import os
from typing import List

from .bid import Bid
import pandas as pd


class AuctionData:
    """
    This class is responsible for loading and packaging the bidding data.
    """
    FILE_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data.csv"

    def __init__(self) -> None:
        """
        The constructor for the AuctionData.
        """
        self._data = []
        self._load_data()

    def _load_data(self) -> None:
        """
        Loads the data from the CSV appending it to self._data.

        :return: None
        """
        df = pd.read_csv(self.FILE_PATH)
        raw_data = df.T.to_dict().values()
        for raw_bid in raw_data:
            new_bid = Bid(account_id=raw_bid["account id"],
                          amount=raw_bid["amount"],
                          auction_id=raw_bid["auction id"],
                          time_unit=raw_bid["time unit"])
            self._data.append(new_bid)

    @property
    def data(self) -> List[Bid]:
        return self._data
