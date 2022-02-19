import generator as gen
import help_functions as help
import math

g = gen.Generator()

print("Wpisz wartosc parametru lambda dla rozkładu wykładniczego (lambda>0): ")
lambd = input()
lambd = float(lambd)
data = list()
probabilities = list()        # prawdopodobienstwo ze x znajduje się w konkretnym przedzile
number_of_attemps = 10000

for i in range(0, number_of_attemps):
    data.append(g.gen_exponential(lambd))

number_of_intervals = math.floor(max(data)) + 1

intervals = help.make_zero_list(number_of_intervals)    # przechowuje ilosc wylosowanych x z kazdego interwalu
expected_numbers = help.make_zero_list(number_of_intervals)

for i in range(0, number_of_attemps):
    intervals[math.floor(data[i])] += 1

for i in range(0, number_of_intervals):
    probabilities.append(gen.exponential_distribuant(lambd, i+1)-gen.exponential_distribuant(lambd, i))
for i in range(0, number_of_intervals):
    expected_numbers[i] = int(probabilities[i]*number_of_attemps)
'''
print("intervals")
for i in range(0, number_of_intervals):
    print("["+str(i)+","+str(i+1)+"]")
print("expected number")
for i in range(0, number_of_intervals):
    print(expected_numbers[i])

print("observed numbers")
for i in range(0, number_of_intervals):
    print(intervals[i])
#'''
chi = 0

for i in range(0, number_of_intervals):
    if expected_numbers[i] != 0:
        chi += (intervals[i] - expected_numbers[i])**2/(expected_numbers[i])

print("statystyka testu chi-kwadrat : "+str(chi))
print("ilosć interwałów "+str(number_of_intervals))
print("ilość stopni swobody "+str(number_of_intervals-2))

# statystyka musi być < wartos graniczną , żeby było OK
# liczba stopni swobody = ilosc przedziałow - ilosc paramentrów rozkładu - 1
# piszemy H0 jeżeli jest OK i H1 jeżeli nie jest ok