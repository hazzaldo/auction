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

def test_adding_invalid_bids_to_auction(create_auction_context):
    print('\n=> Testing adding invalid bids to an auction')
    auction = create_auction_context.get('auction')
    new_bid_1 = Bid.generate()
    new_bid_1.amount = -100
    message_1 = auction.process_bid(new_bid_1)
    error_1 = auction.validate_bid(new_bid_1)
    assert message_1 == auction.get_invalid_bid_message(new_bid_1, error_1)

    new_bid_2 = Bid.generate()
    new_bid_2.auction_id = auction.auction_id+1
    message_2 = auction.process_bid(new_bid_2)
    error_2 = auction.validate_bid(new_bid_2)
    assert message_2 == auction.get_invalid_bid_message(new_bid_2, error_2)

def test_adding_lower_bid_to_auction(create_auction_context):
    print('\n=> Testing adding a lower bid')
    auction = create_auction_context.get('auction')
    bid = create_auction_context.get('bid')
    new_bid = Bid.generate()
    new_bid.amount = bid.amount - 1
    new_bid.auction_id = auction.auction_id
    message = auction.process_bid(new_bid)
    assert new_bid != auction.highest_bid
    assert new_bid not in auction.bids
    assert message == auction.get_insufficient_bid_message(new_bid)

def test_adding_lower_bid_lagging_to_auction(create_auction_context):
    print('\n=> Testing adding a lower bid lagging')
    auction = create_auction_context.get('auction')
    bid = create_auction_context.get('bid')
    new_bid = Bid.generate()
    new_bid.amount = bid.amount - 1
    new_bid.time_unit = bid.time_unit - 1
    new_bid.auction_id = auction.auction_id
    message = auction.process_bid(new_bid)
    assert new_bid != auction.highest_bid
    assert new_bid not in auction.bids
    assert message == auction.get_insufficient_lagging_bid_message(new_bid)
