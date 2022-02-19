import generator as gen
import help_functions as help
from scipy.stats import norm
import math

# test dla rozkładu normalnego

g = gen.Generator()

print("Wpisz wartosc parametru mi (wartosc oczekiwana) dla rozkładu normalnego : ")
mi = input()
mi = float(mi)

print("Wpisz wartosc parametru sigma (odchylenie standardowe) dla rozkładu normalnego: ")
sigma = input()
sigma = float(sigma)

number_of_attemps = 100000
number_of_intervals = 10

probabilities = help.make_zero_list(number_of_intervals)  # prawdopodobienstwo ze x znajduje się w konkretnym przedzile
data = list()
intervals = help.make_zero_list(number_of_intervals)    # przechowuje ilosc wylosowanych x z kazdego interwalu
expected_numbers = help.make_zero_list(number_of_intervals)

for i in range(0, number_of_attemps):
    num = g.gen_normal(mi, sigma)
    data.append(num)

min_num = min(data)
max_num = max(data)
step = math.fabs(max_num-min_num)/number_of_intervals


for i in range(0, number_of_attemps):
    j = 0
    while data[i] >= min_num + j * step:
        j += 1

    if j > number_of_intervals:
        j = number_of_intervals

    intervals[j - 1] += 1

for i in range(0, number_of_intervals):
    probabilities[i] = norm.cdf(min_num+(i+1)*step, mi, sigma) - norm.cdf(min_num+i*step, mi, sigma)

for i in range(0, number_of_intervals):
    expected_numbers[i] = probabilities[i]*number_of_attemps

'''
print("interval ")
for i in range(0, number_of_intervals):
    print("["+str(min_num+i*step)+","+str(min_num+(i+1)*step)+"]")
print("expected number")
for i in range(0, number_of_intervals):
    print(int(expected_numbers[i]))
print("observed numbers")
for i in range(0, number_of_intervals):
    print(intervals[i])
#'''

chi = 0
for i in range(0, number_of_intervals):
    if expected_numbers[i] != 0:
        chi += (intervals[i] - expected_numbers[i])**2/(expected_numbers[i])

print("statystyka testu chi-kwadrat : "+str(chi))
print("ilość stopni swobody: 9")
