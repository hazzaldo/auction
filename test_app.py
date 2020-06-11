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