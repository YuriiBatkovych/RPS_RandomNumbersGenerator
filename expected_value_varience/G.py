import generator as gen

g = gen.Generator()

data = list()

sum = 0
number_of_attemps = 10000  # liczba prób

# poczatek obliczenia wartosci oczekiwane

for i in range(0, number_of_attemps):
    num = g.generate()
    data.append(num)
    sum += num

print("========================")
avr = sum/number_of_attemps

print("wartość estymatora wartości oczekiwanej : "+str(avr))
print("oczekiwana EX : "+str(g.m/2))


# koniec obliczenia wartosci oczekiwane

# poczatek obliczenia wariancji

sum = 0


for i in range(0, number_of_attemps):
    num = g.generate()

    sum += (num - avr)**2

print("========================")
var = sum/(number_of_attemps-1)

print("wartość estymatora wariancji: "+str(var))
print("oczekiwana wariancja : "+str(((g.m+1)**2 - 1)/12))

# koniec obliczenia wariancji

# autokorelacja

r = 100  #przesuniecie ciagu
sum = 0

for i in range(0, number_of_attemps-r):
    sum += (data[i] - avr)*(data[i+r] - avr)

corelation = sum/((number_of_attemps-r)*var)

print("========================")
print("wartość współczynnika autokorelacji dla przesuniecia "+str(r)+" : "+str(corelation))
print("oczekiwana wartość współczynnika autokorelacji: 0 ")