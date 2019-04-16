def isPrime(n):
    if n == 1 or n == 2:
        return True
    else:
        for i in range(2,n-1):
            num = n % i
            if num == 0:
                return '非质数'
        else:
            return '是质数'

try:
    n = int(input("输入一个整数："))
except ValueError:
    print(False)
else:
    print(True)
    print(isPrime(n))