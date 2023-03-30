#Laut der Aufgabestellung String eingeben
string = "Die Mendeleev-Tabelle hat insgesamt einhundertachtzehn Elemente, " \
        "beginnnend mit Wasserstoff(H) und endet mit Oganensson(Og)."
print(string)

# Jedes Element aufsplitten
s_split = string.split(" ")
print(s_split)

# Anzahl der vorhandenen Elementen zaehlen
laenge = len(s_split)
pstring = "Laenge: " + str(laenge)
print(pstring)

# Haufigkeits zaehelen
for word in s_split:
        anzahl = string.count(word)
        mystring = "Anzahl des Wortes: " + str(word) + " lautet: " + str(anzahl)
        print(mystring)

# "." durch "!" ersetzen
nes_string = string.replace(".", "!")
print(string)
print(nes_string)

#String hinzufuegen
s_split.insert(2, ", auch bekannt als Periodensystem der Elemente")
print(s_split)

next_string = ""
for word in s_split:
        next_string = next_string + word + " "
print(next_string)

