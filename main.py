import random
__author__ = 'Yusuke Higuchi'


# Fixme: 1.) What to need: non-player character (NPC) to compete with.
# Fixme: 2.) How user will compete with the NPC. Need to improve if-else logic

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

            dice_six_option = raw_input("\n>>>You got 6. If you don't want to throw a dice, type N<<<")

            if dice_six_option.lower != "n":

                # self.user_num += self.dice_rolled
                # print "\nNow, the total is", self.user_num
                self.dice_play(self.user_num)

            else:
                break

        return self.user_num


player1 = Dice()
player2 = Dice()

player1.user_num = player1.dice_rolled
print "The first dice was", player1.user_num
while player1.user_num == 6:
    input_dice_is_six = raw_input(">>>You got 6. If you don't want to throw a dice, type N<<<")
    if input_dice_is_six.lower() != "n":
        player1.dice_play(player1.user_num)
    else:
        break

user_input = raw_input("\n>>>Enter to throw a dice, s to stop<<<")


while user_input.lower() != "s":

    while player1.dice_rolled == 6:
        input_dice_is_six = raw_input(">>>You got 6. If you don't want to throw a dice, type N<<<")
        if input_dice_is_six.lower() == "n":
            player1.dice_play(player1.user_num)
        else:
            break

    player1.user_num = player1.dice_play(player1.user_num)

    user_input = raw_input("\n>>>Enter to throw a dice, s to quit<<<")


if player1.user_num == 21:
    print "You win!"

else:
    print player1.user_num

# for i in range(0, 6):
#     while player2.dice_rolled == 6:
#         player2.user_num = player2.dice_play(player2.user_num)
#
#     player2.user_num = player2.dice_play(player2.user_num)
