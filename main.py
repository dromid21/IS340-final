from userdice import UserDice
import random


__author__ = 'Yusuke Higuchi'


# Fixme: 1.) What to need: non-player character (NPC) to compete with.
# Fixme: 2.) How user will compete with the NPC. Need to improve if-else logic


player1 = UserDice()    # instantiating player 1

turn_player1 = 1
print "Turn", turn_player1

# the dice_rolled is assigned to the user_score, and print the result
player1.user_score = player1.dice_rolled
print "The first dice was", player1.user_score

# loop if the first dice rolled is 6, otherwise go to the next operation
while player1.user_score == 6:

    # for the first dice giving the user an option to throw a dice
    input_dice_is_six1 = raw_input(">>>You got 6. If you don't want to throw a dice, type S<<<")

    if input_dice_is_six1.lower() != "s":
        player1.dice_play(player1.user_score)
    else:
        break


turn_player1 += 1

# the user can continue to throw a dice
user_input = raw_input("\n>>>Enter to throw a dice, type s to stop<<<")

# loop until the user enter s or S
# from the second dice to the Nth dice are executed
while user_input.lower() != "s":

    print "Turn", turn_player1

    while player1.dice_rolled == 6:
        input_dice_is_six2 = raw_input(">>>You got 6. If you don't want to throw a dice, type S<<<")
        if input_dice_is_six2.lower() != "s":
            player1.dice_play(player1.user_score)
        else:
            break

    # adding a dice_rolled to the cumulative user score
    player1.user_score = player1.dice_play(player1.user_score)

    turn_player1 += 1

    # the user can quit the dice game by entering s
    user_input = raw_input("\n>>>Enter to throw a dice, type s to stop<<<")


if player1.user_score == 21:
    print "\n-->You got 21 in turn %d!" % turn_player1

else:
    print "\n-->Turn %d: your score is %d" % (turn_player1, player1.user_score)


# below is the competitor's play
# the competitor always throw a dice when gets 6

print "\n\n\nNow, move on to your competitor's play"

turn_comp = 1
comp_score = 0

while comp_score <= 17:

    comp_dice_roll = random.randint(1, 6)

    print "\n>>>Competitor's turn %d<<<" % turn_comp

    if comp_dice_roll == 6:
        print "The competitor got 6, and always takes advantage of this chance."
        turn_comp -= 1

    else:
        pass

    # adding a dice_rolled to the cumulative user score
    comp_score += comp_dice_roll

    print "The dice number was", comp_dice_roll
    print "Competitor's score:", comp_score

    turn_comp += 1

if comp_score == 21:
    turn_comp -= 1
    print "\n-->Comp also got 21 in turn %d!" % turn_comp

else:
    turn_comp -= 1
    print "\n-->Turn %d: competitor's score is %d" % (turn_comp, comp_score)

