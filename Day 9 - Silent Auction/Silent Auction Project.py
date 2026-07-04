from art import logo
print(logo)

def add_to_dictionary():
    bids = {}  #empty dictionary

    while True:
        name = input("What's your name? ") #prompt user for name
        bid = int(input("What's your bid? ")) #prompt user for bid

        # store this player's bid
        bids[name] = bid #store the players BID, but not the name.

        other_players = input("Are there any other bids? (yes/no) ").lower() #force lowercase for code to work
        if other_players == "no":
            break
        print("\n" * 20) #make console anonymous

    # find highest bid

    print(f"The winner is {winner} with ${highest_bid}")
add_to_dictionary()