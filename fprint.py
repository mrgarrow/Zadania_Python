# Zadanie 1

separate = '='*40
print(separate,'\n','author: jannowak@poczta.com','\n','date: 05-03-2024','\n',separate,sep='')

# Zadanie 2

separate = '-'*50
nazwa_sklepu = 'ShopIphone'
nazwa_przedmiotu = 'Iphone 15'
cena_przedmiotu = 1000.0
rabat_przedmiotu = 0.30


print('Welcome to',nazwa_sklepu,'\n',separate,sep='')
print("Today's special is the Iphone 15, which normally costs $",cena_przedmiotu,sep='')
print('But for a limited time, you can get it for $',cena_przedmiotu*(1-rabat_przedmiotu),f' ({rabat_przedmiotu*100}% off)!',sep='')

# Zadanie 3

brand = 'Ford'
model = 'Mondeo'
year = '2023'
color = 'Black'
mileage = '8000'

print('CAR DETAILS','\n','Make: ',brand,'\n','Model: ',model,'\n','Year: ',year,'\n','Color: ',color,'\n','Mileage: ',mileage,sep='')

# Zadanie 4

warzywo1 = 'pomidor'
warzywo2 = 'ogórek'
warzywo3 = 'seler'

print(warzywo1,warzywo2,warzywo3,sep=', ')
print(warzywo1,warzywo2,warzywo3,sep='#')
print(warzywo1,warzywo2,warzywo3,sep='-')

# Zadanie 5
# Praktycznie takie samo jak poprzednie

print(warzywo1,warzywo2,warzywo3,'..',sep=',')
print(warzywo1,warzywo2,warzywo3,'…',sep=',')

# Zadanie 6

experiment_name = 'The Effects of Temperature on Enzyme Activity'
treatment_group = 'Group A'
enzyme_activity = 18.3456

print(experiment_name,'',sep='!')
print('The',treatment_group,'enzyme activity level is',round(enzyme_activity,2),'units.')