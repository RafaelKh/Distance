import pandas as pd
from math import cos, asin, sqrt, pi

x = pd.read_excel('/home/rafael/Desktop/testing.xlsx')
a = x.values.tolist()


def distance(lat1, lon1, lat2, lon2):
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a))

l = []
list_of_dist = []
name = input()
for i in a:
    if i[0] == name:
        for j in range(len(a)):
            if a[j][0] != name:
                d = distance(i[1], i[2], a[j][1], a[j][2])
                list_of_dist.append(d)
                l.append([a[j][0], d, a[j][3], a[j][4], a[j][5]])


def heap_sort(a):
    for i in range(1, len(a), 1):
        j = i
        while j > 0 and a[j] > a[(j - 1) // 2]:
            a[j], a[(j - 1) // 2] = a[(j - 1) // 2], a[j]
            j = (j - 1) // 2

    for k in range(0, len(a) - 1, 1):
        a[0], a[len(a) - 1 - k] = a[len(a) - 1 - k], a[0]
        n = 0
        while 2 * n + 1 < len(a) - 1 - k:
            maximum = n
            if a[maximum] < a[2 * n + 1]:
                maximum = 2 * n + 1
            if 2 * n + 2 < len(a) - 1 - k and a[maximum] < a[2 * n + 2]:
                maximum = 2 * n + 2
            if maximum == n:
                break
            else:
                a[maximum], a[n] = a[n], a[maximum]
            n = maximum
    return a


sort = heap_sort(list_of_dist)
names = []
for i in range(5):
    for j in l:
        if sort[i] == j[1]:
            names.append(j[0])
print(names)
