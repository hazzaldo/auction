
class Auction:
    """
    This class is responsible for managing an auction's bids.

    """
    def __init__(self, auction_id: int) -> None:
        """
        The constructor for the Auction class.

        :param auction_id: (int) the ID of the auction that the bid was on
        """
        self.auction_id = auction_id
        self.highest_bid=None 
        self.bids=[]

    def validate_bid(self, bid) -> str:
        """
        Validates the bid
        
        :param bid: (Bid) the bid to validate
        :return: (str) error message if bid is invalid, otherwise empty string
        """
        if bid.auction_id == self.auction_id:
            if not isinstance(bid.time_unit, int):
                return 'Error, bid time unit should be of type integer.'
            elif not isinstance(bid.amount, int):
                return 'Error, bid amount should be of type integer.'
            elif bid.amount < 0:
                return 'Error, bid amount is a negative number. It should be a positive number' 
            else:
                return ''
        else:
            return "Error, the passed bid's auction id does not match the current auction instance's auction id"

        def is_bid_higher(self, bid) -> bool:
        """
        Checks if the incoming bid is higher than the current highest bid
        
        :param bid: (Bid) the incoming bid to check
        :return: (bool) True if incoming bid is higher than current highest bid, otherwise False
        """
        if bid.amount > self.highest_bid or self.highest_bid is None:
            self.highest_bid = bid_amount
            return True
        else:
            return False
