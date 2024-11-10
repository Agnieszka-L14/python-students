name ="Agnieszka"
print("Mam na imię ", name)
# i dodaj jeszcze jakiś ciekawy kod
names=[]

number = int(input("Podaj liczbe imion , które chcesz wprowadzić : " ))
for i in range (number):
    name = input("Podaj imię użytkownika : ")
    names.append(name)
print("Podano nastepujace imiona : ",names)