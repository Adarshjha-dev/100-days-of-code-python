import art

print(art.logo)


def highest_bidder(bids_dict):
    highest_bid = 0
    for bidder in bids_dict:
        bid_amount = bids_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
bidding_over = False

while not bidding_over:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if continue_bidding == "no":
        bidding_over = True
        highest_bidder(bids)
    elif continue_bidding == "yes":
        print("\n" * 25)
