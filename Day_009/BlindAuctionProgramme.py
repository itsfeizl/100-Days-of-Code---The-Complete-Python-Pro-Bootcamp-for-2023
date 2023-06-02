import os
clear = lambda: os.system('cls')
#HINT: You can call clear() to clear the output in the console.

bids = {}

def highest_bidder(bidding_record):
  highest_bid = 0
  
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winning_bidder = bidder
      
  print()    
  print(f"The winning bidder is {winning_bidder} with a highest bid of ${highest_bid}")



continue_bidding = True

while continue_bidding:
  name = input("What is your name? ")
  bid = int(input("What's your bid? $"))
  bids[name] = bid
  print()
  to_continue = input("Are there other bidders? Type 'yes' or 'no': ").lower()
  if to_continue == "no":
    continue_bidding = False
    highest_bidder(bids)
  elif to_continue == "yes":
    clear()
