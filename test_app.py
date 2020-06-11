import pytest
from src.data.auction import Auction
from src.data.bid import Bid

@pytest.fixture(scope="module")
def create_auction_context():
    bid = Bid.generate()
    auction = Auction(bid.auction_id)
    auction.process_bid(bid)
    return {'auction':auction, 'bid':bid}

def test_adding_bid_to_new_auction(create_auction_context):
    print('\n=> Testing adding a bid to a new auction')
    auction = create_auction_context.get('auction')
    assert len(auction.bids)
    assert auction.highest_bid

def test_adding_higher_bid_to_auction(create_auction_context):
    print('\n=> Testing adding a higher bid')
    auction = create_auction_context.get('auction')
    bid = create_auction_context.get('bid')
    new_bid = Bid.generate()
    new_bid.amount = bid.amount + 1
    new_bid.auction_id = auction.auction_id
    message = auction.process_bid(new_bid)
    assert new_bid == auction.highest_bid
    assert new_bid in auction.bids
    assert message == auction.get_accepted_bid_message(new_bid)