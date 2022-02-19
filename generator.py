import numpy as np
import math as math


class Generator:

    def __init__(self):
        self.next = 1
        self.m = 2 ** 32

    def generate(self):  # parametry wzialem od D. Knuth i H.W. Lewis.
        self.next = (1664525 * self.next + 1013904223) % self.m  # generetor G

        return self.next

    def gen_unif(self):
        return self.generate() / self.m  # generator J

    def gen_bernulli(self, p):  # metoda podzialu (0,1) na przedzialy
        attempt = self.gen_unif()

        if attempt <= p:  # generator B
            return 1
        else:
            return 0

    def gen_binominal(self, n, p):  # n prob bernulli o prawdopodob p
        sum = 0
        for i in range(0, n):  # generator D
            sum += self.gen_bernulli(p)

        return sum

    def gen_exponential(self, lambd):  # metoda odwrotnej dystrybuanty
        U = self.gen_unif()

        x = np.log(1 - U) / (-lambd)  # generator W
        return x

    # wykonany za pomoca metody Boxa-Mullera
    def gen_normal(self, mi, sigma):
        U1 = self.gen_unif()
        U2 = self.gen_unif()  # generator N

        Z1 = np.sqrt(-2 * np.log(U1)) * np.cos(2 * np.pi * U2)
      # Z2 = np.sqrt(-2 * np.log(U2)) * np.sin(2 * np.pi * U1)

        x = Z1 * sigma + mi

        return x

    def gen_poisson(self, lambd):  # metoda odwrotnej dystrybuanty dla rozkładu dyskretnego
        U = self.gen_unif()

        x = 0
        e_lambd = np.e ** (-lambd)
        distribuant = e_lambd  # generator P
        while distribuant <= U:
            x += 1
            distribuant += (e_lambd * (lambd ** x)) / (math.factorial(x))

        return x


# Pomocznicze funkcje :

def unif_distribuant(x):  # Dystrybuanta rozkładu jednostajnego na (0, 1)
    if x < 0 or x > 1:
        return 0
    else:
        return x

def G_distribuant(x):     #dystrybuanta równomiernego
    if x < 0 or x > 2**32:
        return 0
    else:
        return x/(2**32)

def exponential_distribuant(lambd, x):
    return 1 - np.e ** (-lambd * x)


def poisson_probability(lambd, x):
    if x < 0 or lambd < 0:
        return 0
    else:
        return (np.e ** (-lambd)) * (lambd ** x) / math.factorial(x)


def binomial_probability(n, p, x):
    return (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))