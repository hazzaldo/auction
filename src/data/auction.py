
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

    def is_bid_lagging(self, bid) -> bool:
        """
        Checks if the incoming bid is lagging
        
        :param bid: (Bid) the incoming bid to check
        :return: (bool) True if incoming bid is lagging, otherwise False
        """
        if bid.time_unit < self.highest_bid.time_unit:
            return True
        else:
            return False

    def process_bid(self, bid: Bid) -> str:
        """
        Processes the bid for a number of outcomes 
        
        :param bid: (Bid) the incoming bid to process
        :return: (str) the bid status message
        """
        bid_status_message = f'Auction ID: {self.auction_id}. Bid by {bid.account_id}. '
        error = self.validate_bid(bid)
        if error:
            return bid_status_message + error
        else:
            if self.is_bid_higher(bid):
                return bid_status_message + f'Bid with amount: {bid.amount} is now the new highest bid'
            elif not self.is_bid_lagging(bid):
                return bid_status_message + f'Bid with amount: {bid.amount} is insufficient.'
            else: 
                return bid_status_message + f'Bid with amount: {bid.amount} is insufficient. Receipt of bid is lagging'
            
        