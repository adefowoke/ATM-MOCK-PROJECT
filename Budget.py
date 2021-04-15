class Budget:
    """
    The Budget class will be used to create objects
    with different categories such as food, clothing, entertainment
    and so on.

    """

    def __init__(self, ):
        """
        This sets the initial value of each category when
        an instance of the class is created. The value in each
        category can be updated either by adding to the value or
        subtracting from it.

        """
        self.food: int = 0
        self.clothing: int = 0
        self.entertainment: int = 0

    def deposit(self, food:int, clothing:int, entertainment:int) -> str:

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
