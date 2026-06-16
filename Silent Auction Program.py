# Silent Auction Program project no 05
# A silent auction is a type of auction where bidders write down their bids on a sheet (or digitally)
# instead of bidding aloud and the values are revealed sometimes after auction completes

import os

def bid_winner(bidder_details) :
    highest_bid = 0
    winner =""
    for bidder in bidder_details :
        bidding_price = bidder_details[bidder]
        if bidding_price > highest_bid :
            highest_bid = bidding_price
            winner = bidder
    print(f"The winner is {winner} with a bid price of {highest_bid}")

bidder_data = {}

bidding_end = False

while bidding_end == False :
    name = input("Enter the name of the bidder :")
    price = int(input(f"Enter {name} bid amount : "))
    bidder_data[name] = price
    bidder = input("Are there more bidder in auction (yes/no) : ").lower()
    if bidder == "no":
        bidding_end = True
        bid_winner(bidder_data)
    elif bidder == "yes":
        os.system("cls")
    else:
        print("INVALID INPUT !!!!!!!! Please type 'yes' or 'no'.")
