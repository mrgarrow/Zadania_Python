# Zadanie 1
# Używając odpowiedniej metody słownikowej dodaj kolejny przedmiot 'english' do zbioru subjects. Otrzymany zbiór wydrukuj do konsoli.

subjects = {'mathematics', 'polish'}
subjects.update({'english'})
print(subjects)

# Zadanie 2

text = 'Programming in python.'

# 1. Wszystkie litery małe.
textlower = text.lower()

# 2. Usunięcie spacji i kropek.
textdelete = textlower.replace(' ', '').replace('.', '')

# 3/4. Zbiór z pozostałych liter i usunięcie samogłosek.
text_rest = []
vowels = {'a', 'e', 'i', 'o', 'u'}

# 1 metoda
for char in textdelete:
    if char not in vowels:
        text_rest.append(char)

remaining = ''.join(text_rest)
print(remaining)

# 2 metoda
for item in vowels:
    textdelete = textdelete.replace(item, '')
print(textdelete)

# 5. Wydrukować liczbę spółgłosek.
count_text = len(remaining)
print('Liczba spółgłosek wynosi: ',count_text)

# Zadanie 3
# Różnica symetryczna zbioru A i B.

set_A = {2,4,6,8}
set_B = {4,10}
sym_diff = set_A.symmetric_difference(set_B)
print('Różnica symetryczna zbiorów A i B to liczby: ',sym_diff)

# Zadanie 4
# Zwróć ID tych klientów, którzy kliknęli w reklamę i kupili produkt. Część wspólna.

clicked_ids = {'9001', '9002', '9005'}
bought_ids = {'9002', '9004', '9005'}
intersec = clicked_ids.intersection(bought_ids)
print('Klienci którzy kliknęli w reklamę i kupili produkt posiadają ID: ',intersec)

# Zadanie 5
# Znów część wspólna.

daily_menu = { 'burger', 'fries', 'hot dog', 'chicken sandwich', 'pasta with seafood'}
fixed_vegetarian_options = { 'fries', 'onion rings', 'pasta with seafood', 'feta salad'}
intersec = daily_menu.intersection(fixed_vegetarian_options)
print('Dania wegetariańskie tego dnia to: ',intersec)