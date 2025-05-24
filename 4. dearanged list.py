lst = input("Enter list elements: ").split()
n = len(lst)
dearanged = lst[1:] + lst[:1] 
i = 0
while i < n:
    if dearanged[i] == lst[i]:
        if i < n - 1:
            dearanged[i], dearanged[i+1] = dearanged[i+1], dearanged[i]
        else:
            dearanged[i], dearanged[i-1] = dearanged[i-1], dearanged[i]
    i += 1

print("Original list:", lst)
print("Dearanged list:", dearanged)