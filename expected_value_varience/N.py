import generator as gen

g = gen.Generator()

data = list()

print("Wpisz wartosc parametru mi (wartosc oczekiwana) dla rozkładu normalnego : ")
mi = input()
mi = float(mi)

print("Wpisz wartosc parametru sigma (odchylenie standardowe) dla rozkładu normalnego: ")
sigma = input()
sigma = float(sigma)
sum = 0
number_of_attemps = 100000  # liczba prób

# poczatek obliczenia wartosci oczekiwane

for i in range(0, number_of_attemps):
    num = g.gen_normal(mi, sigma)
    data.append(num)
    sum += num

print("========================")
avr = sum/number_of_attemps

print("wartość estymatora wartości oczekiwanej : "+str(avr))
print("oczekiwana EX : "+str(mi))

# koniec obliczenia wartosci oczekiwane

# poczatek obliczenia wariancji

sum = 0


for i in range(0, number_of_attemps):
    num = g.gen_normal(mi, sigma)

    sum += (num - avr)**2

print("========================")
var = sum/(number_of_attemps-1)

print("warość estymatora wariancji: "+str(var))
print("oczekiwana wariancja : "+str(sigma**2))

# koniec obliczenia wariancji

# autokorelacja

r = 100  #przesuniecie ciagu
sum = 0

for i in range(0, number_of_attemps-r):
    sum += (data[i] - avr)*(data[i+r] - avr)

corelation = sum/((number_of_attemps-r)*var)

print("========================")
print("warość współczynnika autokorelacji dla przesuniecia "+str(r)+" : "+str(corelation))
print("oczekiwana wartość współczynnika autokorelacji: 0 ")