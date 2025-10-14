auction_logo =  r"""
                         ___________
                                  /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\     
                      """
print(auction_logo)
def highest_bid(bid_dict):
    winner = ""
    highest_bids = 0
    for bidder in bid_dict:
        bid_amt = bid_dict[bidder]
        if bid_amt > highest_bids:
            highest_bids = bid_amt
            winner = bidder
    print(f"The Winner is {winner} with a highest bid of {highest_bids}")

price = {}
players = True
while players:
    name  = input("What is your Name? ")
    bid = int(input("What is your bid $"))
    price[name] = bid
    other_players = input("Are there any other bidders? Type 'Yes' or 'No'").lower()
    if other_players == "no":
        players = False
        highest_bid(price)
    elif other_players == "yes":
        print("\n" * 200)
        print(auction_logo)


