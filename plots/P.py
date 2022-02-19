import generator as gen
import help_functions as help
import matplotlib.pyplot as plt
import numpy as np

g = gen.Generator()

print("Wpisz wartosc parametru lambda dla rozkładu Poissona (lambda>0): ")
lambd = input()
lambd = float(lambd)

number_of_attempts = 10000

nums = list()

for i in range(0, number_of_attempts):
    nums.append(g.gen_poisson(lambd))

min_num = min(nums)
max_num = max(nums)

data = help.make_zero_list(max_num+1)

for i in range(0, number_of_attempts):
    data[nums[i]] += 1

#robimy wykres

plt.xlabel('i')  # etykieta osi x
plt.xticks(np.arange(min_num, max_num, 2))  # zakres wartośći na osi x
plt.ylabel('number of i')  # etykieta osi y
plt.ylim(0, max(data))  # zakres wartośći na osi y
plt.bar(help.make_list(max_num+1), data, label='normal rozklad')  # punkty opisujące funkcje rozkładu
plt.legend()  # wstawiamy legende
plt.show()  # pokazujemy wykres