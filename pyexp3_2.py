def fibonacci(n):
    a = [1,1]
    for i in range(2,n):
        a.append(a[i-1]+a[i-2])
    return a

def sumarr(a):
    sum = 0
    for i in a:
        sum = sum + i
    return sum

array = fibonacci(20)
print(array)
print(sumarr(array))