import random

num_rolls = int(input('Enter number of rolls:\n'))
dice_stats = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}

while num_rolls >= 1:
    for i in range(num_rolls):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll_total = die1 + die2

        dice_stats[roll_total] += 1
        
        print('Roll %d is %d (%d + %d)' % (i, roll_total, die1, die2))

    print('\nDice roll statistics:')
    for stat in dice_stats:
        if stat < 10:
            print("%ds:  %s" % ((stat), ('*' * dice_stats[stat])))
        else:
            print("%ds: %s" % (stat, ('*' * dice_stats[stat])))
    num_rolls = int(input('\nEnter number of rolls:\n'))
else:
    print('Goodbye')
