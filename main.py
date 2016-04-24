import random
__author__ = 'Yusuke Higuchi'


class Dice:
    """
    Creating a class for a dice.
    The user number initially start with a random integer between 1 and 6.
    Then every time dice_play() is called, another random integer is added to the user number.
    """
    def __init__(self):
        self.user_num = random.randint(1, 6)
        self.dice_rolled = random.randint(1, 6)

    def dice_play(self, x):
        """ This is a function for adding numbers.
            When the function is called, the user roll another dice, and add to the current user number.
        """
        self.dice_rolled = random.randint(1, 6)
        print "\nRolled another dice, and the number is", self.dice_rolled
        self.user_num = x + self.dice_rolled
        return self.user_num


dice1 = Dice()
print "Rolled the first dice, and the number is", dice1.user_num
print "Total:", dice1.user_num

while dice1.user_num <= 15:

    dice1.user_num = dice1.dice_play(dice1.user_num)
    print "Total:",
    print dice1.user_num


print "\nYour total number is", dice1.user_num


if dice1.user_num == 21:
    print "You win!"

else:
    user_input = raw_input("\nDo you want to roll a dice, or stop here?"
                           "\nType \"No\" to stop, otherwise you roll a dice")

    if user_input.lower() != "no":
        dice1.user_num = dice1.dice_play(dice1.user_num)
        print "Total:",
        print dice1.user_num

    else:
        print dice1.user_num
