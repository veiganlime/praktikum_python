def main():
    print("uhrsprunglicher String")
    string = "[1,2,3,4, [a, b, c, d], help, run, [[a,b], [1,2]]] \n"
    print(string)

    string = string.strip("\n")
    print(string)

    new_string = string[1:-2]
    print(new_string)

    new_string = new_string.split(",")
    print(new_string)


    index = string.find("[a,b]")

    if index != -1:
        print("Subliste[a,b] wurde an der Stelle gefunden: ", index)
    else:
        print("Subliste[a,b] wurde nicht gefunden")

if __name__ == "__main__":
    main()

