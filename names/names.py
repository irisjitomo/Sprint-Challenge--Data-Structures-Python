import time
from bst import BST

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# theres 2 arrays, names_1 and names_2
# we need to make a BST with insert and contains and import it to names file
binary_search_tree = BST('names')
# loop thru names_1
for names in names_1:
# then binary_search_tree.insert those names
    binary_search_tree.insert(names)
# loop thru names_2
for names2 in names_2:
# then binary_search_tree.contains for those names, if contains
    if binary_search_tree.contains(names2):
# then append to duplicates = []
        duplicates.append(names2)

# original run time was a polynomial: 0(n ** 2)
# runtime now is n log n or even 0(n)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
