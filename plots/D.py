import generator as gen
import help_functions as help
import matplotlib.pyplot as plt
import numpy as np

g = gen.Generator()

print("Wpisz wartosc parametru p dla rozkładu dwumianowego (0<=p<=1): ")
p = input()
p = float(p)

print("Wpisz wartosc parametru n dla rozkładu dwumianowego (n>0): ")
n = input()
n = int(n)

number_of_attempts = 10000

data = help.make_zero_list(n+1)

for i in range(0, number_of_attempts):
    num = g.gen_binominal(n, p)
    data[num] += 1


#robimy wykres

plt.xlabel('i')  # etykieta osi x
plt.xticks(np.arange(0, n+1, 1))  # zakres wartośći na osi x
plt.ylabel('number of i')  # etykieta osi y
plt.ylim(0, max(data))  # zakres wartośći na osi y
plt.bar(help.make_list(n+1), data, label='normal rozklad')  # punkty opisujące funkcje rozkładu
plt.legend()  # wstawiamy legende
plt.show()  # pokazujemy wykres