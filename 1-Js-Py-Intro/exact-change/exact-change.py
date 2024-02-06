denominations = [
    {"value": 100, "singular": "One Hundred Dollar Bill", "plural": "One Hundred Dollar Bills"},
    {"value": 50, "singular": "Fifty Dollar Bill", "plural": "Fifty Dollar Bills"},
    # TODO: Make the rest of these into dicts like those above
    # "Twenty Dollar Bill",
    # "Ten Dollar Bill",
    # "Five Dollar Bill",
    # "Two Dollar Bill",
    # "One Dollar Bill",
    # "Quarter",
    # "Dime"
    # "Nickel",
    # "Penny", 
]

results = []

# Figure out how much of each denomination is in our exact change
for denomination in denominations:
    # Figure out the count
    amount = 5
    results.append[{ "amount": amount, "denomination": denomination }]

# Construct exact change message
second_to_last_index = len(results) - 1
message = ""
for index, item in enumerate(results):
    if item.amount == 1:
        message += f"{item['amount']} {item['denomination']['singular']}"
    else:
        message += f"{item['amount']} {item['denomination']['plural']}"

    if index == second_to_last_index:
        message += f" and "
    else:
        message += ", "

message += "."