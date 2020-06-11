
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
            
    def get_accepted_bid_message(self, bid: Bid) -> str:
        """
        Get the accepted message log for the incoming bid as the new highest bid  
        
        :param bid: (Bid) the incoming bid
        :return: (str) the accepted bid message log
        """
        return f'Auction ID: {self.auction_id}. Bid by {bid.account_id}. Bid with amount: {bid.amount} is now the new highest bid'

    def get_insufficient_bid_message(self, bid: Bid) -> str:
        """
        Get the message log for the incoming bid with insufficient bid   
        
        :param bid: (Bid) the incoming bid
        :return: (str) the insufficient bid message log
        """
        return f'Auction ID: {self.auction_id}. Bid by {bid.account_id}. Bid with amount: {bid.amount} is insufficient.'

    def get_insufficient_lagging_bid_message(self, bid: Bid) -> str:
        """
        Get the message log for the incoming bid with insufficient bid and lagging   
        
        :param bid: (Bid) the incoming bid
        :return: (str) the insufficient and lagging bid message log
        """
        return f'Auction ID: {self.auction_id}. Bid by {bid.account_id}. Bid with amount: {bid.amount} is insufficient.'

    def get_invalid_bid_message(self, bid: Bid, error: str) -> str:
        """
        Get the message log for an invalid bid   
        
        :param bid: (Bid) the incoming bid
        :param error: (str) the error passed from bid validation
        :return: (str) the invalid bid message log
        """
        return f'Auction ID: {self.auction_id}. Bid by {bid.account_id}. ' + error

    def process_bid(self, bid: Bid) -> str:
        """
        Processes the bid for a number of outcomes 
        
        :param bid: (Bid) the incoming bid to process
        :return: (str) the bid status message log
        """
        error = self.validate_bid(bid)
        if error:
            return self.get_invalid_bid_message(self, bid, error)
        else:
            if self.is_bid_higher(bid):
                return self.get_accepted_bid_message(self, bid)
            elif not self.is_bid_lagging(bid):
                return self.get_insufficient_bid_message(self, bid)
            else: 
                return self.get_insufficient_lagging_bid_message(self, bid)