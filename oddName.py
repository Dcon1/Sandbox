"""
Author: Danny Connolly
"""

name = input("Please enter your name")
while name == "":
    name = input("Please enter your name")
for i in range(0, len(name) + 1, 2):
    print(name[i])
