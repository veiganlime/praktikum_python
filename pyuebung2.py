#Aufgabe_1
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
#Aufgabe_2

def main():
        mylist = [[j for j in range(i)] for i in range (10)]
        print(mylist)

        newlist = []
        for element in mylist:
                for e in element:
                        newlist.append(e)
        print(newlist)



if __name__ == "__main__":
    main()
