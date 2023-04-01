L = ['Meier', 'Bauer', 'Moser', 'Molitor', 'Martin']

trittzu = True
for element in L:
    if element[0] != 'M':
        trittzu = False
if trittzu == True:
    print("Alle Namen fangen mit M an!")
else:
    print("Nicht alle Namen fangen mit M an?")
