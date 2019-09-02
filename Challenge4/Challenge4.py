from fibo import fibo
from NumToString import NumToString

x = 1

while x < 10:
    print(str(fibo(x)) + (' - ') + (NumToString(fibo(x))))
    x +=1

