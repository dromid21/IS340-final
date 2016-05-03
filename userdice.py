import random

__author__ = "Yusuke Higuchi"


class UserDice:
    """Contains two methods, __init__ and dice_play

    The first methods __init__ creates two attributes user_score and dice_rolled.
    For details, see "Attributes" below.

    The second methods dice_play returns an integer if the method is called.
    This method include two parameters self and x.
    The parameter x is an integer or an accumulated user_score

    Attributes:
        user_score(int): an integers that accumulates dice numbers
        dice_rolled(int): a random integer between 1 and 6

    """

# this is the first method in class UserDice
    def __init__(self):
        """Initiates the first method.

        The user_score is initially 0, and the first dice number is added to the score.
        The dice number is always an integer between 1 and 6.

        """
        self.user_score = 0
        self.dice_rolled = random.randint(1, 6)

# this is the second method in this UserDice
    def dice_play(self, x):
        """Returns an integer if the method is called.

        This method is used for rolling a dice.
        When this is called, a random number is accumulated to the user_score.

        In this local scope, a random integer is assigned as self.dice_rolled.
        While self.dice_rolled is 6, the user may throw a dice without counting a turn.

        :param self:
        :type: integer:

        :param x: an integer or an accumulated user_score to be added by dice_rolled

        :return: self.user_score: self.user_score = x + self.dice_rolled

        """

        # a random integer is assigned to an object
        self.dice_rolled = random.randint(1, 6)

        print "\nRolled another dice, and the number was", self.dice_rolled

        # Actually adding an argument, the current user_number and the dice rolled during this turn
        self.user_score = x + self.dice_rolled

        print "Your score:", self.user_score

        # loop while the user get 6
        while self.dice_rolled == 6:

            # giving the user an option to throw a dice
            input_dice_is_six = raw_input("\n>>>You got 6. If you don't want to throw a dice, type S<<<")

            # if the user input is not N or n, execute dice_play() method inside itself
            # otherwise, break the loop
            if input_dice_is_six.lower() != "s":

                # self.user_score += self.dice_rolled
                # print "\nNow, the total is", self.user_score
                self.dice_play(self.user_score)

            else:
                break

        return self.user_score


# def comp_dice(x):
#     """Returns an integer if the function is called
#
#     This function is used for the competitor's dice roll.
#
#     When this is called, a random number is accumulated to the comp_score.
#     A random integer is assigned as comp_dice_rolled.
#
#     When getting 6, the competitor always throws a dice without counting a turn.
#
#     :param x: an integer or an accumulated competitor's score
#     :type x: integer
#     :return: comp_score: comp_score = x + comp_dice_rolled
#     :rtype: integer
#
#     """
#
#     # a random integer is assigned to an object
#     comp_dice_rolled = random.randint(1, 6)
#
#     print "\nCompetitor rolled another dice, and the number was", comp_dice_rolled
#
#     comp_score = x + comp_dice_rolled
#     print "The total:", comp_score
#
#     return comp_score
