import random


num_rolls = int(input('Enter number of rolls:\n'))
total_nums = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
roll_total=0

while num_rolls >= 1:
    for i in range(num_rolls):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll_total = die1 + die2
        
        total_nums[roll_total] +=1
        print('Roll %d is %d (%d + %d)' % (i, roll_total, die1, die2))

    print('\nRoll Information')
    for num in total_nums:
        if num < 10:
           print("%ds: %s" % ((num), ('*' * total_nums[num])))
        else:
            print("%ds: %s" % (num, ('*' * total_nums[num])))
        
    num_rolls = int(input('How many times do you want to roll again?(Negavitve number for no)'))
        


else:
    print('Thanks for rolling!')
