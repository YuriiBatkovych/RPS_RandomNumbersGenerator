import generator as gen
import help_functions as help
import math

g = gen.Generator()

print("Wpisz wartosc parametru p dla rozkładu dwumianowego (0<=p<=1): ")
p = input()
p = float(p)

print("Wpisz wartosc parametru n dla rozkładu dwumianowego (n>0): ")
n = input()
n = int(n)
lambd = 0.5

probabilities = list()        # prawdopodobienstwo ze x znajduje się w konkretnym przedzile
number_of_attemps = 10000
number_of_intervals = n+1

intervals = help.make_zero_list(number_of_intervals)    # przechowuje ilosc wylosowanych x z kazdego interwalu
expected_numbers = help.make_zero_list(number_of_intervals)
for i in range(0, number_of_attemps):
    num = g.gen_binominal(n, p)
    intervals[math.floor(num)] += 1

for i in range(0, number_of_intervals):
    probabilities.append(gen.binomial_probability(n, p, i))

for i in range(0, number_of_intervals):
    expected_numbers[i] = int(probabilities[i]*number_of_attemps)
'''
print("intervals")
for i in range(0, number_of_intervals):
    print("["+str(i)+"]")
print("expected number")
for i in range(0, number_of_intervals):
    print(expected_numbers[i])

print("observed numbers")
for i in range(0, number_of_intervals):
    print(intervals[i])
'''

chi = 0

for i in range(0, number_of_intervals):
    chi += (intervals[i] - number_of_attemps*probabilities[i])**2/(number_of_attemps*probabilities[i])

print("statystyka testu chi-kwadrat : "+str(chi))
print("ilość interwałów "+str(number_of_intervals))
print("ilość stopni swobody "+str(number_of_intervals-3))

# statystyka musi być < wartos graniczną , żeby było OK
# liczba stopni swobody = ilosc przedziałow - ilosc paramentrów rozkładu - 1
# piszemy H0 jeżeli jest OK i H1 jeżeli nie jest ok