from replit import clear
#HINT: You can call clear() to clear the output in the console.
def findbidder(auction):
  highest_bid = 0
  for bidder in auction:
    bid = int(auction[bidder])
    if bid > highest_bid:
      highest_bid = bid
      winner = bidder
  print(f"highest bider is {winner} with {highest_bid}")

auction = {}
a = True
while a:
  name = input("Enter your name: ")
  bid = input("Enter your bid: ")
  auction[name] = bid
  clear()
  if input("is there any more bidders: ") == "no":
    a = False
  clear()
  findbidder(auction)