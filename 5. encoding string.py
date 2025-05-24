a = input("Enter a string: ")
r = ""
i = 0
n = len(a)
while i < n:
    count = 1
    while i + 1 < n and a[i] == a[i + 1]:
        count += 1
        i += 1
    if count >= 3:
        r += a[i] + str(count)
    else:
        r += a[i] * count
    i += 1
print("Encoded string:", r)