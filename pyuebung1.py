Liste1 = [3,5,1,4,2,6,10,8,9,7]
Liste2 = ["E", "M", "I", "L", "L", "I", "M", "E", "E", "M"]
Liste3 = [1, 2.0, 3.0, 4, "Text"] * 2


print(Liste1)
print(Liste2)
print(Liste3)

print("Liste1: We are starting with sort")
Liste1.sort()
print(Liste1)
Liste1.sort(reverse=True)
print(Liste1)

print("\n")

print("Liste2: We are starting with sort")
Liste2.sort()
print(Liste2)
Liste2.sort(reverse=True)
print(Liste2)

print("\n")

print("Liste3: We are starting with sort")
try:
    Liste3.sort()
    print(Liste3)
    Liste3.sort(reverse=True)
    print(Liste3)
except:
    print("sort() the array with diverse element is impossible")
print("\n")
print("We adding on 5. place on each array one element, with the same typ as the element before")
Liste1.insert(4, 100)
print(Liste1)
Liste2.insert(4, "second Text")
print(Liste2)
Liste3.insert(4, 3.14)
print(Liste3)

print("Array size")
LaengeListe1 = len(Liste1)
string = "Size of array is:" + str(LaengeListe1)
print(string)
LaengeListe2 = len(Liste2)
string = "Size of array is:" + str(LaengeListe2)
print(string)
LaengeListe3 = len(Liste3)
string = "Size of array is:" + str(LaengeListe3)
print(string)

print("delete element 2")
print("In Liste 1")
print(Liste1)
del Liste1[1]
print(Liste1)
