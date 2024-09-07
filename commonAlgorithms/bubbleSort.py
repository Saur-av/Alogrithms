a = [5,6,3,2,1]
sorted = False
sortLast = 1

while not sorted:
    sorted = True
    for i in range(len(a) - sortLast):
        if a[i] > a[i + 1]:
            sorted = False
            a[i],a[i + 1] = a[i + 1],a[i]
    sortLast += 1

print(a)