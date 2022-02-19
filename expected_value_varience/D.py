import generator as gen

g = gen.Generator()

data = list()

print("Wpisz wartosc parametru p dla rozkładu dwumianowego (0<=p<=1): ")
p = input()
p = float(p)

print("Wpisz wartosc parametru n dla rozkładu dwumianowego (n>0): ")
n = input()
n = int(n)
sum = 0
number_of_attemps = 100000  # liczba prób

# poczatek obliczenia wartosci oczekiwane

for i in range(0, number_of_attemps):
    num = g.gen_binominal(n, p)
    data.append(num)
    sum += num

print("========================")
avr = sum/number_of_attemps

print("wartość estymatora wartości oczekiwanej : "+str(avr))
print("oczekiwana EX : "+str(n*p))

# koniec obliczenia wartosci oczekiwane

# poczatek obliczenia wariancji

sum = 0


for i in range(0, number_of_attemps):
    num = g.gen_binominal(n, p)

    sum += (num - avr)**2

print("========================")
var = sum/(number_of_attemps-1)

print("wartość estymatora wariancji: "+str(var))
print("oczekiwana wariancja : "+str(n*p*(1-p)))

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