# def fizzbuzz(n):
#     array = range(n)
#     for x in array:
#         if (x%3==0):
#              x = 'fizz'
#         print x
#     print array 
#     pass
# fizzbuzz(5)
# we tried to amend an array when we should just push a value to a list

def fizzbuzz(n):
    list = [] 

    for i in range (1,n+1):
        if (i%3) == 0 and (i%5) !=0:
            list.append('Fizz')
        elif (i%5) == 0 and (i%3) !=0:
            list.append('Buzz')
        elif (i%3) == 0 and (i%5) ==0:
            list.append('FizzBuzz')
        else:
            list.append(i)
    return list

fizzbuzz(16)