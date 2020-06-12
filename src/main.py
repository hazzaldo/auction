from data import AuctionData
from data.auction_list import AuctionList
import logging
import os


def main() -> None:
    """
    Runs the main program.

    :return: None
    """

    LOG_FILE = 'log_file.log'
    filedir = os.path.dirname(__file__)
    log_file_path = os.path.join(filedir, LOG_FILE)
    logging.basicConfig(filename=log_file_path, level=logging.INFO)    

    data_handler = AuctionData()
    auctions = AuctionList()
    for bid in data_handler.data:
        message = auctions.process_bid(bid)
        logging.info(message)

    auctions.compile_winning_bids_info()  
    with open('winning_bids_log_file.txt', 'w') as winning_bids_log_file:
        winning_bids_log_file.writelines(auctions.winning_bids_logs)


if __name__ == "__main__":
    main()
