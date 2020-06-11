
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
        self.bids=None

    def validate_bid(self, bid) -> str:
        if bid.auction_id == self.auction_id:
            if not isinstance(bid.amount, int):
                return 'Error, bid amount should be of type integer.'
            elif bid.amount < 0:
                return 'Error, bid amount is a negative number. It should be a positive number' 
            else:
                return ''
        else:
            return "Error, the passed bid's auction id does not match the current auction instance's auction id"

         





