#
#         012345678901234
parrot = "Norwegian Blue"

print(parrot[0:6:2])  #Nre
print(parrot[0:6:3])  #Nw

number="9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
# print(parrot[3:5])
# print(parrot[0:9])
# print(parrot[:9])
# print(parrot[10:14])
# print(parrot[10:])
#
# print(parrot[:6])
# print(parrot[6:])
#
# print(parrot[:6] + parrot[6:])
#
# print(parrot[:])

# print(parrot)
#
# print(parrot[3])
# print(parrot[4])
# print(parrot[9])
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])
# print("!")
# print()
#
# print(parrot[-11])
# print(parrot[-1])
# print(parrot[-5])
# print(parrot[-11])
# print(parrot[-8])
# print(parrot[-6])
# print("!")
# print()
#
# print(parrot[3-14])
# print(parrot[4-14])
# print(parrot[9-14])
# print(parrot[3-14])
# print(parrot[6-14])
# print(parrot[8-14])
# print("!")
# print()
# print()
#           #0123456789012345678901234
# letters = "abcdefghijklmnopqrstuvwxyz"
#
# print(letters[9])
# print(letters[20])
# print(letters[11])
# print(letters[8])
# print(letters[4])
# print()
# print(letters[-23])
# print(letters[-18])
# print(letters[-22])
# print(letters[-7])
# print(letters[-8])
# print(letters[-24])
# print(letters[-19])
