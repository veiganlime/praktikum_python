def rechnen(a, b):
    try:
        return a/b,a,b
    except ZeroDivisionError as e:
        print("Fehler in der Funktion!")
        raise e

class LangweiligeDivision(Exception):
    def __init__(self, a, b):
        self._a = a
        self._b = b
    def __str__(self):
        return "{}/{} ist eine Langweilige Division".format(self._a, self._b)

try:
    a = int(input("Geben Sie den Dividenden ein: "))
    b = int(input("Geben Sie den Divisor ein: "))
    if a == b:
        raise LangweiligeDivision(a, b)
    q = rechnen(a,b)
except LangweiligeDivision as e:
    print(e)
except ZeroDivisionError:
    print("Teilung durch NULL ist nciht erlaubt !")
except Exception as e:
    print("BÄM! - ein Fehler")
    print(type(e))
    print(e.__dict__)
else:
    print("Der Quotient von", a, "und", b, "ist", q)
finally:
    print("ende")