list1 = [1,4,7,3,0,2,7]
print(f"The normal list {list1}")

count = 0
for item in list1:
    count += item
avr = count/len(list1)
print(f"The Average is : {avr}")

list1.sort()
print(f"The smallest element is {list1[0]}")
print(f"The biggest element is {list1[-1]}")