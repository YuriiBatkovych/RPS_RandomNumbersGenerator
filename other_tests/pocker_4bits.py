import generator as gen
import help_functions as help

g = gen.Generator()

number_of_attempts = 20000

nums = list()                         # wygenerowany ciąg zero-jedynkowy
data = help.make_zero_list(16)        # ilosć liczb [0-15]

for i in range(0, number_of_attempts):
    nums.append(g.gen_bernulli(0.5))

iter = 0    # obliczenie ilosc liczb 0-15 (bloki 4-bitowe)
while iter < number_of_attempts:
    num = nums[iter] * 8 + nums[iter + 1] * 4 + nums[iter + 2] * 2 + nums[iter + 3]
    data[num] += 1
    iter += 4

n = int(number_of_attempts/4)    # ilość wszystkich liczb 0-15

# początek obliczenia statystyki testu

sum = 0

for i in range(0, 16):
    sum += data[i]**2

U = (16 * sum)/n - n

print("Wartość statystyki testu =  "+str(U))
