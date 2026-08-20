from art import logo
print(logo)

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

people = {}
bid_over = False
while not bid_over:
    name = input("What is your name?: ")
    price = int(input(f"What is your bid?: $"))
    people[name] = price
    try_again = input("Are there any other bidders? Type 'yes or 'no': ")
    if try_again == 'no':
        bid_over = True
    else:
        print("\n"*100)
        pass

print(people)
highest_bid = 0
winner = ""
for key, value in people.items():
    if highest_bid < value:
        highest_bid = value
        winner = key
print(f"The winner is {key} with a bid of ${value}")