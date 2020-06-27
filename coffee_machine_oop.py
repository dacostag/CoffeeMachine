from collections import Counter

class CoffeeMachine:
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
    main_input_text = "Write action (buy, fill, take, remaining, exit): "

    def __init__(self):
        self.state = "main"
        self.storage = Counter({"water": 400,
                                "milk": 540,
                                "beans": 120,
                                "cups": 9,
                                "money": 550})

    def execute(self, command):
        """ Define the behaviour of the machine based on state and command."""
        main_list = {"buy": self.buy_state, "fill": self.fill_state, "take": self.take, "remaining": self.status, "exit": self.end_program}
        if self.state == "main": return main_list[command]()
        if self.state == "buy": return self.expend(command)
        if self.state.startswith("fill"): return self.fill(command)


    def buy_state(self):
        """ Sets the machine to buy state and returns the appropiate input text."""
        self.state = "buy"
        return "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: "
    
    def expend(self, selection):
        """ Subtract the selected recipe from storage and add the money, set state to main, return main input text."""
        if selection != "back":
            selection = int(selection)        
            for key in self.recipe_book[selection]:
                if self.storage[key] < self.recipe_book[selection][key]:
                    print(f"Sorry, not enough {key}!\n")
                    break
            else:
                print("I have enough resources, making you a coffee!\n")
                self.storage -= self.recipe_book[selection]
    
        self.state = "main"
        return self.main_input_text
    
    def fill_state(self):
        """ Sets the machine to fill state and begins the fill process. """
        self.state = "fill_water"
        return "Write how many ml of water do you want to add: "

    def take(self):
        """ Give all the money available, do not change state, return main input text """
        print(f"I gave you ${self.storage['money']}\n")
        self.storage["money"] = 0
        return self.main_input_text

    def status(self):
        """ Print to terminal the contents of the coffee machine, do not change state, return main input text."""
        print(f"The coffee machine has:\n"
              f"{self.storage['water']} of water\n"
              f"{self.storage['milk']} of milk\n"
              f"{self.storage['beans']} of coffee beans\n"
              f"{self.storage['cups']} of disposable cups\n"
              f"{self.storage['money']} of money\n")
        return self.main_input_text

    def fill(self, selection):
        """ Query the user for amount of each ingredient to add to storage, return storage."""
        selection = int(selection)
        if self.state == "fill_water":
            self.storage["water"] += selection
            self.state = "fill_milk"
            return "Write how many ml of milk do you want to add: "
        elif self.state == "fill_milk":
            self.storage["milk"] += selection
            self.state = "fill_beans"
            return "Write how many grams of coffee beans do you want to add: "
        if self.state == "fill_beans":
            self.storage["beans"] += selection
            self.state = "fill_cups"
            return "Write how many disposable cups of coffee do you want to add: "
        if self.state == "fill_cups":
            self.storage["cups"] += selection
            self.state = "main"
            return self.main_input_text
    
    def end_program(self):  # Unimplemented.
        pass

machine = CoffeeMachine()
input_message = machine.main_input_text
while True:
    command = input(input_message)
    if command == "exit": break
    input_message = machine.execute(command)