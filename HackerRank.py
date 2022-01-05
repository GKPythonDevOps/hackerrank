"""
# *******************************Plus Minus************************
n = 6

def plusMinus(arr):
    # Write your code here
    # l = len(arr)
    zerocount = 0
    positivecount = 0
    negativecount = 0
    if (n > 0 and n <=100):
        for i in range(len(arr)):
            if (arr[i] >= -100 and arr[i] <= 100) :
                if (arr[i] == 0):
                    zerocount += 1
                elif (arr[i] > 0):
                    positivecount +=1
                elif (arr[i] < 0):
                    negativecount +=1


    
    # print(positivecount)
    # print(negativecount)
    # print(zerocount)

    
    print("{0:.6f}".format(positivecount/n))
    print("{0:.6f}".format(negativecount/n))
    print("{0:.6f}".format(zerocount/n))

plusMinus([-4, 3, -9, 0, 4, 1])

#******************************************************************
"""
"""
# *****************************Mini-Max Sum************************
arr = [1,2,3,4,5]
def miniMaxSum(arr):
    
    
        if (min(arr) >=1 and max(arr) <= 10**9):
            arr.sort()
            

            small = arr[1:]
            big = arr[:-1]

            print(str(sum(big))+" "+ str(sum(small)))

#******************************************************************
"""


