import generator as gen
import help_functions as help
import math

g = gen.Generator()

probabilities = list()        # prawdopodobienstwo ze x znajduje się w konkretnym przedzile
number_of_attemps = 10000
number_of_intervals = 10

intervals = help.make_zero_list(number_of_intervals)    # przechowuje ilosc wylosowanych x z kazdego interwalu
expected_numbers = help.make_zero_list(number_of_intervals)

for i in range(0, number_of_attemps):
    num = g.gen_unif()
    intervals[math.floor(num*number_of_intervals)] += 1

for i in range(0, number_of_intervals):
    probabilities.append(gen.unif_distribuant((i+1)/number_of_intervals)-gen.unif_distribuant(i/number_of_intervals))

for i in range(0, number_of_intervals):
    expected_numbers[i] = int(probabilities[i]*number_of_attemps)
'''
print("intervals")
for i in range(0, number_of_intervals):
    print("["+str(i/number_of_intervals)+","+str((i+1)/number_of_intervals)+"]")
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
print("wartość krytyczna dla poziomu istotnośći 0.05 oraz 9 stopni swobody wynosi 16.92")

# statystyka musi być < wartos graniczną , żeby było OK
# liczba stopni swobody = ilosc przedziałow - ilosc paramentrów rozkładu - 1
# piszemy H0 jeżeli jest OK i H1 jeżeli nie jest ok