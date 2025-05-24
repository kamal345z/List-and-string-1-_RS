s1 = input("Enter first string: ").replace(" ", "").lower()
s2 = input("Enter second string: ").replace(" ", "").lower()
if len(s1) != len(s2):
    print("Not anagrams")
else:
    count1 = {}
    count2 = {}
    for char in s1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1
    for char in s2:
        if char in count2:
            count2[char] += 1
        else:
            count2[char] = 1
    if count1 == count2:
        print("Anagrams")
    else:
        print("Not anagrams")