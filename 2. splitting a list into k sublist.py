input_str = input("Enter list elements separated by space: ")
lst = [int(x) for x in input_str.split()]
k = int(input("Enter number of sublists: "))

if k > len(lst):
    print("Cannot split into more sublists than elements.")
else:
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[j] > lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
    sublists = []
    sums = []
    for i in range(k):
        sublists.append([])
        sums.append(0)
    for num in lst:
        min_index = 0
        for i in range(1, k):
            if sums[i] < sums[min_index]:
                min_index = i
        sublists[min_index].append(num)
        sums[min_index] += num
    for i in range(k):
        print("Sublist", i + 1, ":", sublists[i], "sum =", sums[i])