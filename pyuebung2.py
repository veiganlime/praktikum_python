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
#Aufgabe 3
def main ():
        name_dict = { }

        name_dict["Berlin"] = "Deutschland"
        name_dict["London"] = "Grossbritanien"
        name_dict["Washington"] = "USA"
        name_dict["Mexico-City"] = "Mexico"
        name_dict["Moscow"] = "Russische Foederation"
        name_dict["Kiev"] = "Ukraine"
        name_dict["Paris"] = "Frankreich"
        name_dict["Madrid"] = "Spanien"
        name_dict["Amsterdam"] = "Niederlande"
        name_dict["Kopengagen"] = "Daenemark"

        name_dict.update({"Helsinki" : "Finland"})
        print("Elenemten aus Dictionary ausgeben")
        for element in name_dict:
                print(element)

        print("Methode keys, um alle keys auszugeben OHNE for Schleife")
        mylist = list(name_dict.keys())
        # kopieren der Liste der keys, damit wir vorher nachher Vergleiche
        # snstellen koennen
        sorted_list = mylist[:]
        sorted_list.sort()
        print(mylist)
        print(sorted_list)

        for key in sorted_list:
                value = name_dict[key]
                print(value)


if __name__ == "__main__":
    main()
