l1 = input("Enter elements of the list 1 : ").split()
l2 = input("Enter elements of the list 2 : ").split()
intersection = list(set(l1) & set(l2))
print("Intersection is :", intersection)