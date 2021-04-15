class Budget:

    def __init__(self, ):
        self.food = 0
        self.clothing = 0
        self.entertainment = 0

    def deposit(self, food, clothing, entertainment):

        self.food += food
        self.clothing += clothing
        self.entertainment += entertainment
        return (f" this is what is left after deposit food : {self.food}, "
                f"clothing: {self.clothing}, entertainment: {self.entertainment}")

    def withdraw(self, food, clothing, entertainment):
        if self.food >= food:
            self.food -= food
        if self.clothing >= clothing:
            self.clothing -= clothing
        if self.entertainment >= entertainment:
            self.entertainment -= entertainment

    def check_balance(self, ):
        return (f"this is the remaining balance after expenses food : {self.food}, "
                f"clothing: {self.clothing}, entertainment: {self.entertainment}")

    def transfer(self, ):
        pass


budget1 = Budget()
budget1.deposit(50, 30, 20)
budget1.withdraw(10, 15, 5)
print(budget1.check_balance())
