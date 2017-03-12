"""

    getFactors:
        Step 1: generate all prime factors up to sqrt n
        Step 2: iterate through prime factors. Each time we find one, store it as a base.
                Add all the ways to make n / current_factor to the end of this number
        Step 3: Repeat until we're out of factors.

    ISSUES:
        * Generates duplicates
        * Does not list composite factors

"""

def generate_primes(limit):
    if limit < 2: return []
    else:
        primes = [2]
        possible_primes = [2*i + 1 for i in range(1,(limit + 1)//2)]
        for i in range(len(possible_primes)):
            if possible_primes[i] != 0:
                primes.append(possible_primes[i])
                for j in range(i,len(possible_primes),possible_primes[i]):
                    possible_primes[j] = 0
        return primes

def combine_factors(prime,factorings):
    new_factorings = [[prime] + factoring for factoring in factorings if factoring[0] >= prime]
    return new_factorings

def find_factors(n,primes,memo,include_self = True):
    factors = []
    if include_self: factors.append([n])
    if n in primes: return factors
    
    limit = int(ceil(sqrt(n)))
    
    for prime in primes:
        if prime > limit: break
        if n % prime == 0:
            factor = n // prime
            if factor not in memo:
                memo[factor] = find_factors(factor,primes,memo,True)
            factors.extend(combine_factors(prime,memo[factor]))
    return factors

from math import sqrt,ceil

class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        primes = generate_primes(int(ceil(sqrt(n))))
        return find_factors(n,primes,{},include_self = False)
