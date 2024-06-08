# Zadanie 1

import os
filename = '15042024.xlsx'
_,extension = os.path.splitext(filename)
if extension == '.xlsx':
    print('Tak, rozszerzenie tego pliku to .xlsx')
else:
    print('Nie, rozszerzenie tego pliku to nie .xlsx')

# Zadanie 2

passw = 'BLANSDOCSN'

if passw.isupper():
    print('tak')
else:
    print('nie')

# Zadanie 3

flights_ids = ['041524', '126791']
flight_id = '041525'

if flight_id not in flights_ids:
    flights_ids.append(flight_id)
    print(flights_ids)
else:
    print('ID tego lotu już jest zarejestrowane.')

# Zadanie 4

item = '001'
items = ['001', '000', '003', '005', '006']

if item in items:
    items.remove(item)
    print(items)
else:
    print('Tego itemu nie ma na liście.')

# Zadanie 5

sunlight_intensity = 600
if sunlight_intensity <= 200:
    power = 0
    print('chuj')
elif sunlight_intensity <= 400:
    power = 100
elif sunlight_intensity <= 600:
    power = 200
else:
    power = 300

print('Power output of the solar panel is:',power,'watts')

# Zadanie 6

try:
    quiz_score = 80
    if quiz_score < 60:
        print('F')
    elif quiz_score < 70:
        print('D')
    elif quiz_score < 80:
        print('C')
    elif quiz_score < 90:
        print('B')
    else: 
        print('A')
except ValueError:
    print("nieprawidłowe dane wejściowe.")

# Zadanie 7
def getRecomendation(current_price,price_trend,avarage_price):
    if price_trend == 'up' and current_price <= avarage_price:
        return "hold"
    elif price_trend == 'up' and current_price > avarage_price:
        return "buy"
    elif price_trend == 'down' and current_price >= avarage_price:
        return "hold"
    elif price_trend == 'down' and current_price < avarage_price:
        return "sell"
    elif price_trend == 'stable' and current_price <= avarage_price:
        return "buy"
    elif price_trend == 'stable' and current_price > avarage_price:
        return "sell"
    else:
        return "undefined stocks behavior"

print(getRecomendation(10.3, 'up', 32.6))
print(getRecomendation(10.3, 'stable', 1.6))
print(getRecomendation(10.3, 'stable', 32.6))