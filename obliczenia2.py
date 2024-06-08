# Zadanie 1
# Wyznacz środek odcinka o końcach w punktach: A = (2, 4) i B = (-4, 6).

pkta = [2,4]
pktb = [-4,6]
srodek = [(pkta+pktb)/2 for pkta,pktb in zip(pkta,pktb)]
print("Środek odcinka znajduje się w punkcie: ",srodek)

# Zadanie 2
# Oblicz odległość dwóch punktów A=(3, 2), B=(-1, -1) w przestrzeni R^2.

pkta = [3,2]
pktb = [-1,-1]
odcinekab = ((pkta[0]-pktb[0])**2 + (pkta[1]-pktb[1])**2)**(1/2)
print("Długość odcinka wynosi: ",odcinekab)

# Zadanie 3
# Znajdź pierwiastki równania kwadratowego : x^2 +5x +4 =0 .

a = 1
b = 5
c = 4
delta = (b**2) - 4*a*c
if delta > 0:
    deltasqrt = delta**(1/2)
    x1 = (-b + -deltasqrt)/2*a
    x2 = (-b + deltasqrt)/2*a
    print("Pierwiastki równania kwadratowego to:",x1,"oraz",x2)
elif delta == 0:
    x0 = (-b)/(2*a)
    print("Pierwiastkiem równania kwadratowego jest:",x0)
else:
    print("To równanie nie ma pierwiastków kwadratowych.")

# Zadanie 4
# Oblicz średnią geometryczną następującego zestawu liczb: 4, 3, 4.5, 5

def mnozenieTabeli(lista):
    wynik = 1
    for x in lista:
        wynik = wynik*x
    return wynik

liczby = [4,3,4.5,5]
ilosc = len(liczby)
obliczenie = (mnozenieTabeli(liczby))**(1/ilosc)
przyblizenie = "{:.2f}".format(obliczenie)
print("Średnia geometryczna zaokrąglona do 2 miejsc po przecinku wynosi: ",przyblizenie)
#lub
#print("Średnia geometryczna zaokrąglona do 2 miejsc po przecinku wynosi: ","%.2f"%obliczenie)
#lub
#print("Średnia geometryczna zaokrąglona do 2 miejsc po przecinku wynosi: ",round(obliczenie,2))

# Zadanie 5
# Oblicz odchylenie standardowe następującego zestawu danych: 10, 11, 9

def dodawanieTabeli(liczby):
    wynik = 0
    for x in liczby:
        wynik = wynik+x
    return wynik

def licznik(liczby):
    wynik = 0
    for x in liczby:
        wynik += (x-sredniaArytm)**2
    return wynik

liczby = [10,11,9]
ilosc = len(liczby)
sredniaArytm = (dodawanieTabeli(liczby)/ilosc)
odchylenie = (licznik(liczby)/ilosc)**(1/2)
print("Odchylenie standardowe dla zadanych liczb wynosi: ",round(odchylenie,2))