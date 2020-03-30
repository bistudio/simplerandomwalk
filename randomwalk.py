import random as rnd

direction = list('NSEW')


def randomwalk(blocks):
    """define a function that returns cumulative coordinates of a random walk of n blocks"""
    x, y = (0, 0)
    for i in range(blocks):
        if rnd.choice(direction) == 'N':
            y += 1
        elif rnd.choice(direction) == 'S':
            y -= 1
        elif rnd.choice(direction) == 'E':
            x += 1
        else:
            x -= 1
    return x, y


for w in range(25):
    walk = randomwalk(10)
    distance = abs(walk[0]) + abs(walk[1])
    print(f'walk: {w}, distance from home: {distance}')
