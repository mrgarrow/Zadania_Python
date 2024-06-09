#Zadanie 1

spacers = 50*'='
menu = '> Main Menu'
print (spacers, menu, spacers,sep='\n')
list = [('1.','View all products'),('2.','Search for a product'),('3.','Add a new product'),('5.','Delete a product'),('7.','Checkout'),('8.','Exit')]
for x,y in list:
    print(x,y,sep='\t')

# Zadanie 4

indexes = [ 'WIG', 'WIG-banki', 'WIG-budownictwo', 'WIG-CEE', 'WIG-chemia', 'WIGenergia', 'WIG-ESG', 
           'WIG-górnictwo', 'WIG-informatyka', 'WIG-leki', 'WIG-media',
            'WIG-motoryzacja', 'WIG-nieruchomości', 'WIG-odzież', 'WIG-paliwa', 'WIG-Poland',
            'WIG-spożywczy', 'WIG-telekomunikacja', 'WIG-Ukraine', 'WIG.GAMES', 'WIG.MS-BAS',
            'WIG.MS-FIN', 'WIG.MS-PET', 'WIG20', 'WIG20dvp', 'WIG20lev', 'WIG20short',
            'WIG20TR', 'WIG30', 'WIG30TR', 'WIGdiv', 'WIGtech',]
for item in indexes:
    if '30' in item or '20' in item:
        print(item)

num_of_cars = 400
num_of_parts = 1900
cost_per_part = 40
profit_per_car = 900

# Zadanie 5
file = open('products.txt','r')
lines = file.read().splitlines()
for x in lines[1:len(lines)]:
    print(x.split(sep=';'))

# Zadanie 6

call_records = [ { 'name': 'John', 'phone': '123456789', 'duration': 30,
'cost': 5.0, },
{ 'name': 'Jane', 'phone': '234567890', 'duration': 90, 'cost':
10.0, },
{ 'name': 'John', 'phone': '345678901', 'duration': 120, 'cost':
15.0, },
{ 'name': 'Alice', 'phone': '456789012', 'duration': 45, 'cost': 7.5, },
{ 'name': 'John', 'phone': '567890123', 'duration': 75, 'cost': 9.0, },]
total_duration = 0
for record in call_records:
    if record['name'] != 'John'or record['duration'] < 60:
        continue
    total_duration += record['duration']
print(total_duration)

# zadanie 7

stock_data = { 'AAPL': 145.9,
'GOOG': 2680.7,
'TSLA': 712.6,
'AMZN': 3379.1}

with open('stock_prices.txt','w') as writer:
    for key in stock_data:
        writer.write(key)
        writer.write(';')
        writer.write(str(stock_data[key]))
        writer.write('\n')
        print(writer)