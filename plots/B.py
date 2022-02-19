import generator as gen
import help_functions as help
import matplotlib.pyplot as plt
import numpy as np

g = gen.Generator()

print("Wpisz wartosc parametru p dla rozkładu Bernulliego (0<=p<=1): ")
p = input()
p = float(p)

number_of_attempts = 10000

data = help.make_zero_list(2)

for i in range(0, number_of_attempts):
    num = g.gen_bernulli(p)
    data[num] += 1


#robimy wykres
plt.xlabel('i')  # etykieta osi x
plt.xticks([0, 1])# zakres wartośći na osi x
plt.ylabel('number of i')  # etykieta osi y
plt.ylim(0, number_of_attempts)  # zakres wartośći na osi y
plt.bar(help.make_list(2), data)  # punkty opisujące funkcje rozkładu
plt.legend()  # wstawiamy legende
plt.show()  # pokazujemy wykres