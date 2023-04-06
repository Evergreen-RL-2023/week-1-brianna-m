'''
computing averages and 1-armed bandit

3 ways to compute averages
The third method uses temporal difference
see Sutton and Barto
Q = Q + a*(R - Q), where in this case Q is the average
and R is the new value to be averaged

also use rand.gauss(0, 1) instead of i

'''

import random as rand

N = 2

def average1():
    sum = 0
    for i in range(1, N):
        sum += i
    avg = sum / (N-1)
    print('avg1', avg)

def average2():
    avg = 0
    for i in range(1, N):
        avg = avg * (i-1)/i + 1
    print('avg2', avg)

def average3():
    avg = 0
    for i in range(1, N):
        avg = i #fix this
    print('avg3', avg)


if __name__ == '__main__':
    average1()
    average2()
    average3()
    
