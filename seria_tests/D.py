import generator as gen
import help_functions as help

g = gen.Generator()

print("Wpisz wartosc parametru p dla rozkładu dwumianowego (0<=p<=1): ")
p = input()
p = float(p)

print("Wpisz wartosc parametru n dla rozkładu dwumianowego (n>0): ")
n = input()
n = int(n)

random_numbers = list()
number_of_attempts = 30

for i in range(0, number_of_attempts):
    random_numbers.append(g.gen_binominal(n, p))

median = help.find_median(random_numbers)
print("Mediana : " + str(median))
data = list()     # lista symboli 1 (jęzeli odpowiadający mu wygenerowana liczba losowa < mediane)
                                        # i 0 (jeżeli > mediane)

numberOfOnes = 0
numberOfZeros = 0
for i in range(0, number_of_attempts):
    if random_numbers[i] < median:
        data.append(0)
        numberOfZeros += 1
    elif random_numbers[i] > median:
        data.append(1)
        numberOfOnes += 1


dataLen = len(data)
prev = data[0]
numberOfseries = 1    # ilosc serii

for i in range(1, dataLen):
    if data[i] != prev:
        numberOfseries += 1

    prev = data[i]


print("Serie : ")
print(data)

print("Ilość serii (statystyka testu) : "+str(numberOfseries))
print("Ilość ogólna symboli 0 : " + str(numberOfZeros))
print("Ilość ogólna symboli 1 : " + str(numberOfOnes))
