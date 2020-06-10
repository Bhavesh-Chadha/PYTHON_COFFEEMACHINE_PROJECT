#creating a class based on coffee machine bacause all operations in this project are to b done on and by coffee machine
class COFFEEMACHINE:

#creating a constructor which will create attributes indicating state of ingredients needed for different instances of order 
    
    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money
# method to tells the state of ingredients in coffee machine at any instance
    def coffee_machine(self):  # remaining

        print()
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")
        print()
        
#method that creates coffe acc. to the order

    def coffee_make(self, menu):

        if self.water < menu.water:
            print("Sorry, not enough water!")
        elif self.milk < menu.milk:
            print("Sorry, not enough milk!")
        elif self.coffee_beans < menu.coffee_beans:
            print("Sorry, not enough coffee beans!")
        elif self.cups < menu.cups:
            print("Sorry, not enough cups!")
        else:
            self.water = self.water - menu.water
            self.milk = self.milk - menu.milk
            self.coffee_beans = self.coffee_beans - menu.coffee_beans
            self.cups = self.cups - menu.cups
            self.money = self.money - menu.money
        print()
# method to take  order
    def coffee_buy(self):

        print()
        coffee_buy = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
#here order will sent to make function  which will tell the function the ncessary amount of ingredients it will need to complete the operation 
      
        if coffee_buy == "1":
            ingredient.coffee_make(espresso)
        elif coffee_buy == "2":
            ingredient.coffee_make(latte)
        elif coffee_buy == "3":
            ingredient.coffee_make(cappuccino)
            
#method that let the owner to refill the machine

    def coffee_fill(self):

        print()
        fill_water = int(input("Write how many ml of water do you want to add: "))
        self.water += fill_water
        fill_milk = int(input("Write how many ml of milk do you want to add: "))
        self.milk += fill_milk
        fill_cobean = int(input("Write how many grams of coffee beans do you want to add: "))
        self.coffee_beans += fill_cobean
        fill_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
        self.cups += fill_cups
        print()

#method that allows owner to takeout the money machine have made 
    def coffee_take(self):

        print()
        print(f"I gave you ${self.money}")
        print()
        self.money -= self.money

#method which perform the start operation
    def coffee_start(self):
        while True:
            question = input("Write action (buy, fill, take, remaining, exit): ")
            if question == "buy":
                ingredient.coffee_buy()
            elif question == "fill":
                ingredient.coffee_fill()
            elif question == "take":
                ingredient.coffee_take()
            elif question == "remaining":
                ingredient.coffee_machine()
            elif question == "exit":
                break

ingredient = COFFEEMACHINE(400, 540, 120, 9, 550)
espresso = COFFEEMACHINE(250, 0, 16, 1, -4)
latte = COFFEEMACHINE(350, 75, 20, 1, -7)
cappuccino = COFFEEMACHINE(200, 100, 12, 1, -6)

ingredient.coffee_start()