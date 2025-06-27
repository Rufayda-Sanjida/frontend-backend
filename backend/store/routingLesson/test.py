string = "ten-ducks-enter-local-pond"

myList = list(string)
newString = ""

for x in myList:
    if x == "-":
        newString = newString + " "
    else:
        newString = newString + x

print(string)
print(myList)
print(newString)