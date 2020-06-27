from collections import Counter


def status(storage):
    """ Print to terminal the contents of storage."""
    print(f"The coffee machine has:\n"
          f"{storage['water']} of water\n"
          f"{storage['milk']} of milk\n"
          f"{storage['beans']} of coffee beans\n"
          f"{storage['cups']} of disposable cups\n"
          f"{storage['money']} of money\n")

def buy(storage, selection):
    """ Request a selection, subtract the recipe from storage and add the money."""
    
    r1 = Counter({"water": 250,
                  "milk": 0,
                  "beans": 16,
                  "cups": 1,
                  "money": -4})
    r2 = Counter({"water": 350,
                  "milk": 75,
                  "beans": 20,
                  "cups": 1,
                  "money": -7})
    r3 = Counter({"water": 200,
                  "milk": 100,
                  "beans": 12,
                  "cups": 1,
                  "money": -6})

    recipe_book = (Counter(), r1, r2, r3)

    for key in recipe_book[selection]:
        if storage[key] < recipe_book[selection][key]:
            print(f"Sorry, not enough {key}!\n")
            break
    else:
        print("I have enough resources, making you a coffee!\n")
        storage -= recipe_book[selection]

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

current_storage = Counter({"water": 400,
                           "milk": 540,
                           "beans": 120,
                           "cups": 9,
                           "money": 550})


while True:
    action = input("Write action (buy, fill, take, remaining, exit): ") # Don't actually need to specify "remaining"
    if action == "buy":
        selection = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        print()
        if selection.isnumeric():
            current_storage = buy(current_storage, int(selection))
    elif action == "fill":
        current_storage = fill(current_storage)
    elif action == "take":
        current_storage = take(current_storage)
    elif action == "remaining":
        status(current_storage)
    elif action == "exit":
        break
    print()

