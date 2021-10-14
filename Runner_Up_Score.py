"""

Runner-Up Score! :- Need to sort second highest number in list

Input :-

n = 5
arr = 2 3 6 6 5

Condition:
2 <= n <=10
-100 <= a[i] <=100
"""


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    
if n > 1 and n<11:
    
    l = list(arr) # Convert MAP into List --------> [2, 3, 6, 6, 5]
    l.sort(reverse=True) # Sort the list in reverse order ==> Desc -----------> [6, 6, 5, 3, 2]
    a = l[0] # First element of the list. which will be the max number in list. ----------> [6]
    
    c = 0
    for b in l:
        if b > -101 and b < 101:
            if b ==a:
                pass
            elif b !=a:
                c = b
                break
    
    print(c) # second highest number in list --------------> 5