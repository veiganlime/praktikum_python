import sys

def schaltjahr(eingabe):
    if eingabe < 1583:
        return None
    return eingabe % 4 == 0 and eingabe % 100 != 0 or eingabe % 400 == 0

print("Das ist ein Startmeldung!")

try:
    eingabe = int(input("Geben Sie ein Jahr ein!"))
except ValueError:
    print("Eingegebenen Wert ist kein Zahl!")
    sys.exit(1)

isSchaltjahr = schaltjahr(eingabe)

if isSchaltjahr:
    print(eingabe, "ist ein Schaltjahr")
elif isSchaltjahr is None:
    print("Jahr entspricht nicht dem Gregorianischen Kalender")
else:
    print(eingabe, "- ist kein Schaltjahr")