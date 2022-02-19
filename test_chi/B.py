import generator as gen
import help_functions as help
import math

g = gen.Generator()
print("Wpisz wartosc parametru p dla rozkładu Bernulliego (0<=p<=1): ")
p = input()
p = float(p)

probabilities = help.make_zero_list(2)  # prawdopodobienstwo ze x znajduje się w konkretnym przedzile
probabilities[0] = 1-p
probabilities[1] = p

number_of_attemps = 10000
number_of_intervals = 2

intervals = help.make_zero_list(number_of_intervals)    # przechowuje ilosc wylosowanych x z kazdego interwalu

for i in range(0, number_of_attemps):
    num = g.gen_bernulli(p)
    intervals[num] += 1

chi = 0

for i in range(0, number_of_intervals):
    chi += (intervals[i] - number_of_attemps*probabilities[i])**2/(number_of_attemps*probabilities[i])

print("ilość zer "+str(intervals[0]))
print("ilość jedynek "+str(intervals[1]))

print("statystyka testu chi-kwadrat : "+str(chi))
print("wartość krytyczna dla poziomu istotnośći 0.05 oraz 1 stopnia swobody wynosi 3.841")

# statystyka musi być < wartos graniczną , żeby było OK
# liczba stopni swobody = ilosc przedziałow - ilosc paramentrów rozkładu - 1