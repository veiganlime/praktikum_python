#liste and Tupel
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