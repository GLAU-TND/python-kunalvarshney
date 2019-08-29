n = int (input("enter number of bottles : "))

list1 = []
for i in range(0 , n):
    list1.append(int(input("")))

print(list1)

list2=sorted(list1)
print(list2)

count = 0
d={}

d = {x:list2.count(x) for x in list2}
print(d)
print(max(d.values()), " --------answer-------", max(d.keys()))
a = max(d.keys())
print(a)