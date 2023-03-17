#Liste and Tupel
la = [1, 2, 3, 4]
lb = la
print("Liste vorher:", id(la), id(lb))
la += [5]
print(lb)
print("Liste nachher:", id(la), id(lb))
print()

ta = (1, 2, 3, 4)
tb = ta
print("Tupel vorher:", id(ta), id(tb))
ta += (5,)
print(tb)
print("Tupel nachher:", id(ta), id(tb))




# Dictionary
waehrung = {
    "Deutschland" : "Euro",
    "USA" : "US Dollar",
    "England" : "Pfund",
    "Japan" : "Yen"
}
kontostand = {
    "Maier" : "123.45",
    "Mueller" : "7854.54",
    "Schulze" : "4567,89"
}
leeresDictionary = { }
nochEinLeeresDictionary = dict()

print("Dictionary ID vorher", id(waehrung))
waehrung["Russland"] = "Rubel"
print("Dictionary ID nachher", id(waehrung))
print(waehrung["Russland"])
print()



print("Muellers Kontostand", kontostand["Mueller"])
kontostand["Mueller"] = 0
print("Muellers Kontostand nach der Aenderung", kontostand["Mueller"])
kontostand["Mueller"] = -99
print("Muellers Kontostand nach der 2. Aenderung", kontostand["Mueller"])
