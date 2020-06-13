import pytest
from src.data.auction import Auction
from src.data.bid import Bid
from src.data.auction_list import AuctionList

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
    assert message == auction.get_accepted_bid_message(new_bid.account_id, new_bid.amount)

def test_adding_invalid_bids_to_auction(create_auction_context):
    print('\n=> Testing adding invalid bid to an auction')
    auction = create_auction_context.get('auction')
    new_bid_1 = Bid.generate()
    new_bid_1.amount = -100
    message_1 = auction.process_bid(new_bid_1)
    error_1 = auction.validate_bid(new_bid_1)
    assert message_1 == auction.get_invalid_bid_message(new_bid_1.account_id, error_1)

    new_bid_2 = Bid.generate()
    new_bid_2.auction_id = auction.auction_id+1
    message_2 = auction.process_bid(new_bid_2)
    error_2 = auction.validate_bid(new_bid_2)
    assert message_2 == auction.get_invalid_bid_message(new_bid_2.account_id, error_2)

def test_adding_lower_bid_to_auction(create_auction_context):
    print('\n=> Testing adding a lower bid')
    auction = create_auction_context.get('auction')
    bid = create_auction_context.get('bid')
    new_bid = Bid.generate()
    new_bid.time_unit = auction.latest_processed_bid.time_unit + 1
    new_bid.amount = bid.amount - 1
    new_bid.auction_id = auction.auction_id
    message = auction.process_bid(new_bid)
    assert new_bid != auction.highest_bid
    assert new_bid not in auction.bids
    assert message == auction.get_insufficient_bid_message(new_bid.account_id, new_bid.amount)

def test_adding_lower_bid_lagging_to_auction(create_auction_context):
    print('\n=> Testing adding a lower bid lagging')
    auction = create_auction_context.get('auction')
    bid = create_auction_context.get('bid')
    new_bid = Bid.generate()
    new_bid.time_unit = auction.latest_processed_bid.time_unit - 1
    new_bid.amount = bid.amount - 1
    new_bid.auction_id = auction.auction_id
    message = auction.process_bid(new_bid)
    assert new_bid != auction.highest_bid
    assert new_bid not in auction.bids
    assert message == auction.get_insufficient_lagging_bid_message(new_bid.account_id, new_bid.amount)

@pytest.fixture(scope="module")
def create_auction_list_context():
    bid = Bid.generate()
    auction_list = AuctionList()
    auction_list.process_bid(bid)
    return {'auction_list':auction_list, 'bid':bid}

def test_creating_auction_list(create_auction_list_context):
    print('\n=> Testing creating new auction list')
    auction_list = create_auction_list_context.get('auction_list')
    bid = create_auction_list_context.get('bid')
    assert len(auction_list.auctions)
    assert auction_list.auctions[0].auction_id == bid.auction_id

def test_adding_bid_to_auction_list(create_auction_list_context):
    print('\n=> Testing adding a new bid to the auctions')
    auction_list = create_auction_list_context.get('auction_list')
    bid = create_auction_list_context.get('bid')
    new_bid = Bid.generate()
    new_bid.auction_id = bid.auction_id + 1
    auction_list.process_bid(new_bid)
    new_auction = auction_list.get_auction_by_id(new_bid.auction_id)
    assert new_auction
    assert new_auction.auction_id == new_bid.auction_id