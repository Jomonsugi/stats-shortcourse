#!/usr/bin/env python


##########################################################################
## Can you prove that De Morgan's laws work in Python?
##########################################################################

a = set(["A","B","C","D"])
b = set(["C","D","E","F"])
sample_space = set(["A","B","C","D","E","F","G"])

## The complement of the union of two sets is the same as the intersection of their complements
part1 = sample_space.difference(a.union(b))
part2 = sample_space.difference(b).intersection(sample_space.difference(a))
print(part1==part2)

## The complement of the intersection of two sets is the same as the union of their complements
part1 = sample_space.difference(b).union(sample_space.difference(a))
part2 = sample_space.difference(a.intersection(b))
print(part1==part2)

##########################################################################
## combinations and permutations
##########################################################################
from math import factorial
from itertools import combinations,permutations
from scipy.misc import comb

## We have sampler plates that hold 4 beers.  How many different ways can we combine these beers?
lefthand_beers = ["Milk Stout", "Good Juju", "Fade to Black", "Polestar Pilsner"]
lefthand_beers += ["Black Jack Porter", "Wake Up Dead Imperial Stout","Warrior IPA"]
n = len(lefthand_beers)
k = 4

def comb(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

print("There are %s combinations"%comb(n,k))
    
## Print a list of these pairs so we can identify the bad ones?
for c in combinations(lefthand_beers,4):
    print(c)

## on a team of 12 baseball players how many batting orders?    
print("batting orders: %s"%count)

def permu(n,k):
    return factorial(n) / factorial(n - k)

print(permu(12,9))

##########################################################################
## probability
##########################################################################

## probability of a queen
p_queen = 1.0/52 + 1.0/52 + 1.0/52 + 1.0/52
p_queen_or_spade = 4.0/52 + 13/52 - 1.0/52 
