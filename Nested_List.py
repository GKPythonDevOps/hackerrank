
if __name__ == '__main__':
    for _ in range(int(input())):
        records = {}
        name = input()
        score = float(input())
        records[name]=score




"""
My Input while Building the code

records = [["Harry",37.21],["Berry",37.21],["Tina",37.2],["Akriti",41],["Harsh",39]]

records.sort()
print(records)
"""

d = {}
m = []
for a in records:
    "a = ['Harry', 37.21]"
    d[a[0]]=a[1]
    m.append(a[1])

m.sort()
h = m[0]
s = 0
for n in m:
    if n > h:
        s =n
        break
    else:
        pass

for q in d:
    if d[q] == s:
        print(q)
    
    else:
        pass


