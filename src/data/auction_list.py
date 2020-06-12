from data.auction import Auction
from data.bid import Bid
import logging

class AuctionList:
    """
    This class is responsible for processing the outcome auctions' bids.

    """
    def __init__(self) -> None:
        """
        The constructor for the AuctionList class.
        """
        self.auctions = []
        self.winning_bids_logs = []
    
    def compile_winning_bids_info(self) -> None:
        """
        Compile all th winning bids into message logs and append them to 'winning_bids_logs' instance variable List object
        """
        for auction in self.auctions:
            if auction.highest_bid is None:
                self.winning_bids_logs.append(f'For Auction: {auction.auction_id} - no valid bid was received \n')
            else:
                self.winning_bids_logs.append(f'For Auction: {auction.auction_id} - Account: {auction.highest_bid.account_id} won the bid of amount: {auction.highest_bid.amount} \n')

    def get_auction_by_id(self, id: int) -> Auction:
        """
        Get an existing or create a new auction object matching the passed bid's auction ID
        
        :param bid: (int) the auction id of the bid to find the matching Auction 
        :return: (Auction) the matching auction object by auction ID
        """
        found_auction = list(filter(lambda auction: auction.auction_id == id, self.auctions))
        auction = None
        if found_auction:
            auction = found_auction[0]   
        else:
            auction = Auction(id)
            self.auctions.append(auction)
        return auction
            

    def process_bid(self, bid: Bid) -> str:
        """
        Process the outcome of the bid to output a message log
        
        :param bid: (Bid) the incoming bid 
        :return: (str) the output message log for the bid
        """
        matching_auction = self.get_auction_by_id(bid.auction_id)
        bid_messsage_log = matching_auction.process_bid(bid)
        return bid_messsage_log

