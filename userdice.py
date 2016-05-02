import random

__author__ = "Yusuke Higuchi"


class UserDice:
    """
    Creating a class for a dice.
    The user_score is initially 0, and the first dice number is added to the score.
    The dice number is always an integer between 1 and 6.
    Then every time dice_play() is called, another random integer is added to the user_score.
    """

# this is the first method in class UserDice
    def __init__(self):
        self.user_score = 0
        self.dice_rolled = random.randint(1, 6)

# this is the second method in this UserDice
    def dice_play(self, x):
        """
        This is a function for playing a dice roll and adding a number to the current user score.
        When this method is called, a random integer is assigned as dice_rolled, and then add to user_score.
        While that integer is 6, the user is allowed to threw another dice in the same turn.
        """

        # a random integer is assigned to an object
        self.dice_rolled = random.randint(1, 6)

        print "\nRolled another dice, and the number was", self.dice_rolled

        # Actually adding an argument, the current user_number and the dice rolled during this turn
        self.user_score = x + self.dice_rolled

        print "The total:", self.user_score

        # loop while the user get 6
        while self.dice_rolled == 6:

            # giving the user an option to throw a dice
            input_dice_is_six = raw_input("\n>>>You got 6. If you don't want to throw a dice, type N<<<")

            # if the user input is not N or n, execute dice_play() method inside itself
            # otherwise, break the loop
            if input_dice_is_six.lower() != "n":

                # self.user_score += self.dice_rolled
                # print "\nNow, the total is", self.user_score
                self.dice_play(self.user_score)

            else:
                break

        return self.user_score


def comp_dice(x):

    # a random integer is assigned to an object
    comp_dice_rolled = random.randint(1, 6)

    print "\nCompetitor rolled another dice, and the number was", comp_dice_rolled

    # Actually adding an argument, the current user_number and the dice rolled during this turn
    comp_score = x + comp_dice_rolled

    print "The total:", comp_score

    # loop while the user get 6
    while comp_dice_rolled == 6:

        # giving the user an option to throw a dice
        print "The competitor got 6, and always takes advantage of this chance."

        comp_dice(comp_score)

    return comp_score
