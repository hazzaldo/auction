from typing import Dict
import random


class Bid:
    """
    This class is responsible for managing the data for a bid.

    Attributes:
        account_id (int): the ID of the account making a bid
        amount (int): the amount that the bid was for
        auction_id (int): the ID of the auction that the bid was on
        time_unit (int): time unit of when the bid was made
    """
    account_id: int
    amount: int
    auction_id: int
    time_unit: int

    def __init__(self, account_id: int, amount: int, auction_id: int, time_unit: int) -> None:
        """
        The constructor for the Bid class.

        :param account_id: (int) the ID of the account making a bid
        :param amount: (int) the amount that the bid was for
        :param auction_id: (int) the ID of the auction that the bid was on
        :param time_unit: (int) time unit of when the bid was made
        """
        self.account_id = account_id
        self.amount = amount
        self.auction_id = auction_id
        self.time_unit = time_unit

    @property
    def package(self) -> Dict[str, int]:
        """
        Packages the bid into a dict.

        :return: (dict) bid data
        """
        return {
            "account id": self.auction_id,
            "amount": self.amount,
            "auction id": self.auction_id,
            "time unit": self.time_unit
        }

    @classmethod
    def generate(cls):
        """
        Generates a random bid.

        :return: (Bid) random bid
        """
        account_id = random.randint(0, 10)
        amount = random.randint(0, 20000)
        auction_id = random.randint(0, 20)
        time_unit = random.randint(0, 100)
        return cls(account_id=account_id, amount=amount, auction_id=auction_id, time_unit=time_unit)
