# Guessing game
# write a program where your program generate a random number, and the player have to guess it within 5 terms
# if he correctly guess it within 5 times, he wins or he fails

# Ikra's solution:

from random import randint

a = randint(1, 30)

l = 1
has_won = False
while l <= 5:
    n = int(input('Type a number up to 30|Number of tryings:%s|' %(l)))
    if n == a:
        print('You WON!')
        has_won = True
        break
    else:
        print("Sorry it's not the exact number")
    l += 1

if has_won == False:
    print('Sorry you have lost!')
    print('Real num was ',a)
