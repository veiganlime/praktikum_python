def main():
    # leere Liste erzeugen
    myList = []
    myList.append("Katze")
    myList.append("Hund")
    myList.append("Super")
    myList.append("17")
    myList.append("3.14")
    print(myList)

    myList[2] = 123
    print(myList)

    myList.append("Ni")
    myList.extend([1, 2, 3])
    myList.append([1, 2, 3])
    myList.append(3.14)
    print(myList)

    myList.insert(2, "Taube")
    print(myList)

    anzahl = myList.count(3.14)
    print(anzahl)

    index = myList.index(3.14)
    print(index)
    index = myList.index("3.14")
    print(index)
    index = myList.index(3.14, 6)
    print(index)
    myList.remove(3.14)
    print(myList)




if __name__ == "__main__":
    main()
