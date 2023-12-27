bid_window = []
new_bid = {}
winner = []
bid_status = False
winner = {"name": "none", "bid": 0}

def bidding(a, b):
    
    new_bid["name"] = a
    new_bid["bid"] = b
    bid_window.append(new_bid)


while bid_status == False:
    name = str(input("What is your name?: "))
    bid = int(input("What is your bid?: "))
    status = str(input("More bid?: "))
    bidding(name, bid)
    if new_bid["bid"] > winner["bid"]:
        winner = new_bid

    if status == "no":
        bid_status = True
        print(winner)

