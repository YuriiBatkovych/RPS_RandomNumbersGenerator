import generator as gen
import help_functions as help
import math

g = gen.Generator()

probabilities = list()        # prawdopodobienstwo ze x znajduje się w konkretnym przedzile
number_of_attemps = 10000
number_of_intervals = 10
step = g.m/number_of_intervals
expected_numbers = help.make_zero_list(number_of_intervals)

intervals = help.make_zero_list(number_of_intervals)

for i in range(0, number_of_attemps):
    num = g.generate()
    j=0
    while num > j*step:
        j += 1
    intervals[j-1] += 1

for i in range(0, number_of_intervals):
    probabilities.append(gen.G_distribuant((i+1)*step)-gen.G_distribuant(i*step))

for i in range(0, number_of_intervals):
    expected_numbers[i] = probabilities[i]*number_of_attemps

'''
print("intervals")
for i in range(0, number_of_intervals):
    print("["+str(int(i*step))+","+str(int((i+1)*step))+"]")
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
