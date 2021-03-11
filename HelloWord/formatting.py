for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))    # Right justified (automatic)

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))  # ^ center

print()

print("Pi is approximately {0:12}".format(22 / 7))      # Defaults to 15 decimals
print("Pi is approximately {0:12f}".format(22 / 7))     # 6 digits after decimal
print("Pi is approximately {0:2.50f}".format(22 / 7))   # Float format precision 50
print("Pi is approximately {0:52.50f}".format(22 / 7))  # Float format precision 50
print("Pi is approximately {0:62.50f}".format(22 / 7))  # Float format precision 50
print("Pi is approximately {0:<72.50f}".format(22 / 7)) # Float format precision 50
print("Pi is approximately {0:<72.54f}".format(22 / 7))

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))   # < Left justified

print()