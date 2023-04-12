'''
Brianna Manolopoulos
Advanced Computing - Reinforcement Learning
Spring 2023
Week 1

computing averages and 1-armed bandit

3 ways to compute averages
3 ways with gaussian-distributed random values
'''

import random as rand

N = 1000

def average1():
    sum = 0
    for i in range(1,N):
        sum += i

    mean = sum / (N -1)
    print('avg1: ', mean)

def average1_gaus():
    sum = 0
    for i in range(1, N):
        # sum += rand.gauss(0,1)
        # guassian distribution with mean 0 and standard deviation 1
        sum += rand.gauss(0,1)

    mean = sum / (N - 1)
    print('avg1_gaus: ', mean)

def average2():
    '''
    avg[i] = ((i-1)/i) * avg[i-1] + (1/i) * v[i]
    '''
    avg = 0
    for i in range(1, N):
        avg = avg * (i - 1)/i + (1/i * i)
    print('avg2: ', avg)

def average2_gaus():
    '''
    avg[i] = ((i-1)/i) * avg[i-1] + (1/i) * v[i]
    '''
    avg = 0
    for i in range(1, N):
        avg = avg * (i - 1)/i + (1/i * rand.gauss(0,1))
    print('avg2_gaus: ', avg)

def average3():
    '''
    avg[i] = avg[i-1] + (proportional) step_size * difference between
    randomly-generated reward and the previoius average
    '''
    avg = 0
    for i in range(1, N):
        avg = avg + (1/i) * (i - avg)
    print('avg3: ', avg)

def average3_gaus():
    '''
    avg[i] = avg[i-1] + (proportional) step_size * difference between
    randomly-generated reward and the previoius average
    '''
    avg = 0
    for i in range(1, N):
        avg = avg + (1/i) * (rand.gauss(0,1) - avg)
    print('avg3_gaus: ', avg)


if __name__ == '__main__':
    average1()
    average2()
    average3()

    average1_gaus()
    average2_gaus()
    average3_gaus()
