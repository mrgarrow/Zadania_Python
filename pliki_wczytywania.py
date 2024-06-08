# Zadanie 1

# metoda 1
with open('num.txt','w') as file:
    for i in range(1,10):
        number = i*2
        file.write(str(number)+'\n')
# metoda 2
    # for i in range(1,20):
    #     if i % 2 != 1:
    #         file.write(str(i)+'\n')

# Zadanie 2

with open('playway.txt','r') as file:
    closeSum = 0
    # closeCount = 0

    content = file.readlines()
    header = content[0]
    data = content[1:len(content)]
    for line in data:
        _, _, _, _, close, _ = line.split(',')  
        closeSum += int(close)
        # closeCount += 1

    print(round(closeSum/len(data),2))

# Zadanie 3

with open('data.csv','r') as file:
    energySum = 0

    content = file.readlines()
    header = content[0]
    data = content[1:len(content)]
    for line in data:
        _, _, energy = line.split(',')  
        energySum += float(energy)

    print(round(energySum/len(data),2),"kWh")
