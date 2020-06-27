
def status(storage):
    """ Print to terminal the contents of storage."""
    print(f"The coffee machine has:\n"
          f"{storage['water']} of water\n"
          f"{storage['milk']} of milk\n"
          f"{storage['beans']} of coffee beans\n"
          f"{storage['cups']} of disposable cups\n"
          f"{storage['money']} of money\n")

def buy(storage, recipe):
    """ Subtract the recipe from storage and add the money."""
    if recipe == "1":
        storage["water"] -= 250
        storage["beans"] -= 16
        storage["cups"] -= 1
        storage["money"] += 4
    elif recipe == "2":
        storage["water"] -= 350
        storage["milk"] -= 75
        storage["beans"] -= 20
        storage["cups"] -= 1
        storage["money"] += 7
    elif recipe == "3":
        storage["water"] -= 200
        storage["milk"] -= 100
        storage["beans"] -= 12
        storage["cups"] -= 1
        storage["money"] += 6
    return storage

def fill(storage):
    """ Query the user for amount of each ingredient to add to storage, return storage."""
    storage["water"] += int(input("Write how many ml of water do you want to add: "))
    storage["milk"] += int(input("Write how many ml of milk do you want to add: "))
    storage["beans"] += int(input("Write how many grams of coffee beans do you want to add: "))
    storage["cups"] += int(input("Write how many disposable cups of coffee do you want to add: "))
    print()
    return storage

def take(storage):
    """ Give all the money available. """
    print(f"I gave you ${storage['money']}")
    storage["money"] = 0
    print()
    return storage

current_storage = {"water": 400,
                   "milk": 540,
                   "beans": 120,
                   "cups": 9,
                   "money": 550}

status(current_storage)
action = input("Write action (buy, fill, take, remaining, exit): ")
if action == "buy":
    selection = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
    current_storage = buy(current_storage, selection)
elif action == "fill":
    current_storage = fill(current_storage)
elif action == "take":
    current_storage = take(current_storage)
status(current_storage)


