# Zadanie 1

pi = 3.14
r = 5
area = pi*(r**2)
print('The area of the circle is:',area,'cm2')

# Zadanie 2

amount = 1000
percentage = 0.03
years = 5
amount_sum = round(amount*(1+percentage)**years,2)
print(f"The final value of the investment is: {amount_sum} PLN")

# metoda 2
# sum = amount
# for years in range(1,years+1):
#     sum += sum *percentage
# sum = round(sum, 2)
# print(f"The final value of the investment is: {sum} PLN")

# metoda 3
# current = 1
# while current <=5:
#     total = amount+(amount*percentage)
#     current += 1
#     amount = total
# print(f"The final value of the investment is: {round(amount,2)} PLN")

# Zadanie 3

a = 3
b = -4
c = 1
delta = (b**2) - 4*a*c
print('The value of delta is:',delta)

# Zadanie 4

n=1
total = 0
while n <= 10:
    an = 10 + 4*n
    total += an
    n +=1
print('The sum of the first 10 terms of the sequence is: ',total)

# Zadanie 5

n=1
total = 0
while n <= 6:
    an = 8-2**(n-1)
    total += an
    n +=1
print('The sum of the first 6 numbers is: ',total)

# Zadanie 6

a = 1
b = 4
c = 5

sum_x = -(b/a)
product_x = c*a
print(f'x1 + x2 = {sum_x}')
print(f'x1*x2 = {product_x}')

