"""

Runner-Up Score! :- Need to sort second highest number in list

Input :-

n = 5
arr = 2 3 6 6 5
"""


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    
if n > 1 and n<11:
    
    a = list(arr)
    #a.sort()
    z = max(a)
    v = 0
    for b in a:
        if b > v and b < z :
            v = b
    
    print(v)