import time

from BST import BST

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# this solution is 0(n ^ 2)

BST = BST('names')

for name1 in names_1:
    BST.insert(name1)
for name2 in names_2:
    if BST.contains(name2):
        duplicates.append(name2)




end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

# This solution is 0(n) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!

n1 = set(names_1)
n2 = set(names_2)

duplicates = n1.intersection(n2)