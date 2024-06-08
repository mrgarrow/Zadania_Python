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

import numpy as np
import matplotlib.pyplot as plt

year = [1990, 1995, 2000, 2005, 2010]
avg_salary = [3300, 3700, 4200, 4400, 4950]
plt.plot(year, avg_salary)

plt.show()