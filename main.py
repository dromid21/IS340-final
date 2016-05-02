import random

__author__ = 'Yusuke Higuchi'


# Fixme: 1.) What to need: non-player character (NPC) to compete with.
# Fixme: 2.) How user will compete with the NPC. Need to improve if-else logic

class Dice:
    """
    Creating a class for a dice.
    The user_score is initially 0, and the first dice number is added to the score.
    The dice number is always an integer between 1 and 6.
    Then every time dice_play() is called, another random integer is added to the user_score.
    """

# this is the first method in class Dice
    def __init__(self):
        self.user_score = 0
        self.dice_rolled = random.randint(1, 6)

# this is the second method in this Dice
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
            dice_six_option = raw_input("\n>>>You got 6. If you don't want to throw a dice, type N<<<")

            # if the user input is not N or n, execute dice_play() method inside itself
            # otherwise, break the loop
            if dice_six_option.lower != "n":

                # self.user_score += self.dice_rolled
                # print "\nNow, the total is", self.user_score
                self.dice_play(self.user_score)

            else:
                break

        return self.user_score


player1 = Dice()    # instantiating player 1
player2 = Dice()    # instantiating player 2

turn = 1
print "Turn", turn

# the dice_rolled is assigned to the user_score, and print the result
player1.user_score = player1.dice_rolled
print "The first dice was", player1.user_score

# loop if the first dice rolled is 6, otherwise go to the next operation
while player1.user_score == 6:

    # for the first dice giving the user an option to throw a dice
    input_dice_is_six1 = raw_input(">>>You got 6. If you don't want to throw a dice, type N<<<")
    if input_dice_is_six1.lower() != "n":
        player1.dice_play(player1.user_score)
    else:
        break


turn += 1

# the user can continue to throw a dice
user_input = raw_input("\n>>>Enter to throw a dice, type s to stop<<<")

# loop until the user enter s or S
# from the second dice to the Nth dice are executed
while user_input.lower() != "s":

    print "Turn", turn

    while player1.dice_rolled == 6:
        input_dice_is_six2 = raw_input(">>>You got 6. If you don't want to throw a dice, type N<<<")
        if input_dice_is_six2.lower() != "n":
            player1.dice_play(player1.user_score)
        else:
            break

    # adding a dice_rolled to the cumulative user score
    player1.user_score = player1.dice_play(player1.user_score)

    turn += 1

    # the user can quit the dice game by entering s
    user_input = raw_input("\n>>>Enter to throw a dice, type s to stop<<<")


if player1.user_score == 21:
    print "You win!"

else:
    print player1.user_score
