import sys
print("Das ist ein Startmeldung, hello")

try:
    print("Geben Sie biite die Zahl ein!")
    eingabe = int(input())
    print("Sie haben folgenden Jahr  eingegeben:", eingabe)
except ValueError:
    print("Eingabe ist kein int")
    sys.exit(1)
if eingabe < 1:
    print("Jahr entspricht nicht dem Gregorianischen Kalender")
    sys.exit(1)

jahr_pruefen =   eingabe % 4 == 0 and eingabe % 100 != 0 or eingabe % 400 == 0

if jahr_pruefen:
    print(eingabe, "ist ein Schaltjahr")
else:
    print(eingabe, "ist kein Schaltjahr")