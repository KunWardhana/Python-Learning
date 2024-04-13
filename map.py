import find_map as fm

cities = ['Ashcalon', 'Borimir', 'Caenafen', 'Domina', 'Ehlnofey']

Path = {
    ('Ashcalon', 'Borimir') : 4,
    ('Ashcalon', 'Caenafen') : 2,
    ('Borimir', 'Caenafen') : 1,
    ('Borimir', 'Domina') : 2,
    ('Caenafen', 'Domina') : 4,
    ('Caenafen', 'Ehlnofey') : 5,
    ('Ehlnofey', 'Domina') : 1,
}

print("Map of illudia  " + "######################" + "\n")
for x in cities:
    print(x)
print("\n" + "######################" + "\n")

end = input('Hail Traveler!, Where do you wish to go? ')
start = input('Where are you now? ')

print("It will take: " + str(fm.find(cities, Path, start, end)) + " Days, brace yourself.")
