def WordMatching(li):
    list1 = []
    count = 0
    for item in li:
        if len(item) > 1 and item[0] == item[-1]:
            count += 1
            list1.append(item)
    return count
print(f"\nThere are {WordMatching(["aba", "bic", "adga", "9348979"])} item that have same information at the start and the end\n")