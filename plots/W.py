import generator as gen
import help_functions as help
import matplotlib.pyplot as plt

g = gen.Generator()

print("Wpisz wartosc parametru lambda dla rozkładu wykładniczego (lambda>0): ")
lambd = input()
lambd = float(lambd)

number_of_attems = 2000

data = list()
attempts = help.make_list(number_of_attems)


for i in range(0, number_of_attems):
    num = g.gen_exponential(lambd)
    data.append(num)

min_num = min(data)
max_num = max(data)

#robimy wykres
plt.figure(figsize=(16, 10), dpi= 80, facecolor='w', edgecolor='k')
plt.xticks(fontsize=12); plt.yticks(fontsize=12)
plt.xlabel('attempt')  # etykieta osi x
plt.xlim(0, number_of_attems)  # zakres wartośći na osi x
plt.ylabel('value of variable')  # etykieta osi y
plt.ylim(min_num, max_num)  # zakres wartośći na osi y
plt.scatter(attempts, data, label='normal rozklad')  # punkty opisujące funkcje rozkładu
plt.legend()  # wstawiamy legende
plt.show()  # pokazujemy wykres