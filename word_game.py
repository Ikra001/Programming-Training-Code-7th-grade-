# Problem: Create a word game where player one inputs a valid word, and player two have to input a valid word containing the last letter
# of the player one's input as the first letter, the game continues untill one of the player fails to input a correct word within 15 seconds

#ikra's solution

import time

n = input('Player 1: ')
m = input('Player 2: ')

na = len(n)
ma = len(m)

if n[na - 1] == m[0]:
    print('OK')
else:
    print('Player 2 FAILED!')

l = 0
ne = n[l]
me = m[l]

while n[na-1] == m[0]:
    start = time.time()
    n = input('Player 1: ')
    end = time.time()
    if (end - start > 15):
        print('Player 1 FAILED to answer within 15 seconds | YOU WASTED ',int(end - start),' SECONDS')
        break
    na = len(n)
    if m[ma-1] == n[0]:
        print('OK')
    else:
        print('Player 1 FAILED!')
        break

    start = time.time()
    m = input('Player 2: ')
    end = time.time()
    if (end - start > 15):
        print('Player 2 FAILED to answer within 15 seconds')
        break
    ma = len(m)
    if n[na-1] == m[0]:
        print('OK')
    else:
        print('Player 2 FAILED!')
        break
