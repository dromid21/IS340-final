import random
__author__ = 'Yusuke Higuchi'


class Dice:
    """
    Creating a class for a dice.
    The user number initially start with a random integer between 1 and 6.
    Then every time add_dice() is called, another random integer is added to the user number.
    """
    def __init__(self):
        self.user_num = random.randint(1, 6)
        self.dice_rolled = random.randint(1, 6)

    def add_dice(self):
        """ This is a function for adding numbers.
            When the function is called, the user roll another dice, and add to the current user number.
        """
        self.user_num = self.user_num + self.dice_rolled
        return self.user_num

dice1 = Dice()
print dice1.user_num

print "Dice rolled", dice1.dice_rolled
new_num = dice1.add_dice()
print new_num

print "Another dice rolled", dice1.dice_rolled
new_num = dice1.add_dice()
print new_num


