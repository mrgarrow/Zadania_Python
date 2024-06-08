# Zadanie 1

array = []

for i in range(10,100):
    if i % 11 == 0:
        array.append(str(i))
print(','.join(array))

# Zadanie 2 

password = 'cskdnjcasa#!'

if len(password) >= 11:
    print('Password is valid!')
else:
    print('Password is too short!')

# Zadanie 3

# metoda 1
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]

for value in probabilities[:]:
    if value < 0.5:
        probabilities.remove(value)
print(probabilities)

# metoda 2
# def value_above(value):
#     return value > 0.5
# filtered_probs = list(filter(value_above,probabilities))
# print(filtered_probs)

# Zadanie 4 

def prime_values(values):
    if values < 2:
        return False
    for i in range(2, int(values ** 0.5) + 1):
        if values % i == 0:
            return False
    return True
primes = []
values = 2
count = 0

while True:
    if prime_values(values):
        primes.append(values)
        count += 1
        if count == 10:
            break
    values += 1
print(','.join(map(str, primes)))

# Zadanie 5

pv = 1000
r = 0.04
expect_value = pv*2
fv = 0
n = 0

while fv <= expect_value:
    fv=pv+(pv*r)
    n += 1
    pv=fv
print('Future value: ' + str(round(fv,2)), "Number of periods: " + str(n), sep='\n')

# Zadanie 6

limit = 100

A = 1
B = 0

currentValue = 0

array2 = []

while currentValue < limit:
    currentValue = A + B
    B = A
    A = currentValue
    array2.append(str(B))
print(','.join(array2))