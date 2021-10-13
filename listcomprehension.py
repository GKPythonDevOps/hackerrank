x = 1
y = 1
z = 1
n = 2
"""
s = sum([x,y,z])

r = s*n

lst = [[] for _ in range(r+1)]

ilist = [[n]for n in range(x+1) for _ in range_list(round(r/2)-1) ]
"""

s = sum([x,y,z])

r = s*n

def range_list(rr):
    
    lst = [[] for _ in range(rr+1)]
     
    return lst

def i(x):
    ilist = []
    
    for n in range(x+1):
        for m in range_list(round(r/2)-1):
            m.append(n)
            ilist.append(m)
            
    return ilist
    
def j(y):
    jlist = []
   
    for n in range(y+1):
        for m in range_list(round(r/4)-1):
            m.append(n)
            jlist.append(m)

    for n in range(y+1):
        for m in range_list(round(r/4)-1):
            m.append(n)
            jlist.append(m)

    return jlist


def k(z):
    zlist = []
 
    i=0
    while i < r:   
        for n in range(z+1):
            zlist.append([n])
        
        i = i+1

                   
    return zlist 

"""
print(i(x))
print(j(y))
print(k(z))
"""
f_list = []
q =0 
while q < r:
    for w in i(x):
        """
        f_list.append(w+k(z)[q]+j(y)[q])
        """
        f_list.append(w+j(y)[q]+k(z)[q])
        q = q+1

print(f_list)
final_list = []
for g in f_list:
    if sum(g) != n:
        final_list.append(g)

print(final_list)




