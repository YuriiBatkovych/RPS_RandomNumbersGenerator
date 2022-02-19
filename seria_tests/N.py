import generator as gen
import help_functions as help


g = gen.Generator()

print("Wpisz wartosc parametru mi (wartosc oczekiwana) dla rozkładu normalnego : ")
mi = input()
mi = float(mi)

print("Wpisz wartosc parametru sigma (odchylenie standardowe) dla rozkładu normalnego: ")
sigma = input()
sigma = float(sigma)

random_numbers = list()
number_of_attempts = 35

for i in range(0, number_of_attempts):
    random_numbers.append(g.gen_normal(mi, sigma))

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
