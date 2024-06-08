# Zadanie 1
# Suma obiektów.

wig20 = ('CDR', 'PKO', 'PEO')
mwig40 = ('PLW', 'AMC', 'BFT')
suma = wig20 + mwig40
print(suma)

# Zadanie 2
# Liczba 'YES'.

default_settings = ('YES', 'NO', 'NO', 'YES', 'NO')
count = default_settings.count('YES')
print("Number of 'YES': ",count)

# Zadanie 3
# Wyciąć 'PLW'.

stocks = [ ('Playway', ('PLW', 310)), ('CD Projekt', ('CDR', 300))]
skrot = stocks[0][1][0]
print('Skrót Playway to: ',skrot)

# Zadanie 4 
# Dodać gdańsk na końcu listy i wydrukować.

cities = ['Warszawa', 'Łódź', 'Kraków']
mod_cities = cities.append('Gdańsk')
print(cities)

# Zadanie 5
# Operacje na listach.

import unicodedata
# Znaleziona w internecie metoda ale nie działa poprawnie
# def stand_text(text):
#     low_text = text.lower()
    #  moded_text = unicodedata.normalize('NFD',low_text)
#     standed_text = ''.join(char if unicodedata.category(char) != 'Mn' else 'e' for char in moded_text)
#     return standed_text
# text = 'Programowanie w języku Python'
# standed_text = stand_text(text)
# print(standed_text)

text = 'Programowanie w języku Python'
low_text = text.lower()
norm_text = low_text.replace('ę','e')
unique_chars = list(set(norm_text))
unique_chars.remove(' ')
unique_chars.sort()
print(unique_chars[0:10])

# Zadanie 6
# Wydrukować godziny

flights = [
['United Airlines','UA123','New York','Los Angeles','10:00 AM'],
['Delta Airlines','DL456','Chicago','Houston','11:30 AM'],
['American Airlines','AA789','Dallas','San Francisco','08:15 AM'],
['Southwest Airlines','WN012','Los Angeles','Denver','09:45 AM']
]
data = [row[4] for row in flights]
print(data)

# Zadanie 7
# Utworzyć słownik

cc = {
    'Poland':'Warsaw',
    'Germany':'Berlin',
    'Austria':'Vienna'
}
print(cc)

# Zadanie 8
# Rozszerzyć listy.

players = ['LeBron', 'Kobe', 'Jordan']
scores = [27, 18, 15]

new_players = ['LeBron', 'Kobe']
new_scores = [27, 18]

expanded_players = players + new_players
expanded_scores = scores + new_scores
print(expanded_players,expanded_scores, sep="\n")

# Zadanie 9 
# Wyodrębnić dane.

stocks = {
'PLW': {'Playway': 316},
'CDR': {'CD Projekt': 293},
'TEN': {'Ten Square Games': 301}
}

price = stocks['TEN']['Ten Square Games']
print('Wartość akcji spółki Ten Square Games: ',price)

# Zadanie 10
# 

itinerary = {
'destination': 'Paris, France',
'duration': 7,
'budget': 1500,
'activities': ['Visit the Eiffel Tower','Explore the Louvre','Take a Seine River Cruise']
}
itinerary.update({'duration':10})
itinerary['activities'].append('Visit the Palace of Versailles')
itinerary['accommodation'] = 'Hotel'
itinerary['activities'] = len(itinerary['activities'])

toBePrinted = ['destination','duration','budget','activities']

for key in toBePrinted:
    print(key + ":" + str(itinerary[key]))

# for key,value in itinerary.items():
#     if key != 'accommodation':
#         print(key + ':',value)
