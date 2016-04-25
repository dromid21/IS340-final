import random
__author__ = 'Yusuke Higuchi'


# Fixme: 1.) need non-player character (NPC) to compete with.
# Fixme: 2.) better to have an option to threw a dice when getting 6
# Fixme: 3.) if-else statement, lines between 64 and 77, is incomplete

class Dice:
    """
    Creating a class for a dice.
    The user number initially start with a random integer between 1 and 6.
    Then every time dice_play() is called, another random integer is added to the user number.
    """
    def __init__(self):
        self.user_num = 0
        self.dice_rolled = random.randint(1, 6)

    def dice_play(self, x):
        """
        This is a function for adding numbers.
        When the function is called, the user roll another dice, and add to the current user number.
        """
        self.dice_rolled = random.randint(1, 6)

        print "\nRolled another dice, and the number was", self.dice_rolled

        self.user_num = x + self.dice_rolled
        # Actually adding an argument, the current user_number and the dice rolled during this turn

        print "The total:", self.user_num

        while self.dice_rolled == 6:
            # a user keep rolling a dice while continuously getting 6
            self.user_num += self.dice_rolled
            print "Your dice was 6, and you can threw a dice again." \
                  "\nNow, the total is", self.user_num

            self.dice_play(self.user_num)

        return self.user_num


player1 = Dice()
player1.user_num = player1.dice_rolled
print "The first dice was", player1.user_num
while player1.user_num == 6:
    player1.dice_play(player1.user_num)


user_input = raw_input("\n>>>Enter 1 to roll a dice<<<")


while user_input == "1":

    while player1.dice_rolled == 6:
        player1.user_num = player1.dice_play(player1.user_num)

    player1.user_num = player1.dice_play(player1.user_num)

    user_input = raw_input("\n>>>>>Enter 1 to roll a dice<<<<<")


if player1.user_num == 21:
    print "You win!"

else:
    user_input = raw_input("\nDo you want to roll a dice, or stop here?"
                           "\nType \"No\" to stop, otherwise you roll a dice")

    if user_input.lower() != "no":
        player1.user_num = player1.dice_play(player1.user_num)
        print "Total:",
        print player1.user_num

    else:
        print player1.user_num
