def fibonacci(a):
    if a <= 0:
        return "Invalid number"
    elif a == 1:
        return 0
    elif a == 2:
        return 1
    else:
        return fibonacci(a-1) + fibonacci(a-2)


a = int(input("Enter number of terms: "))

print("Fibonacci Series:")
for i in range(1, a+1):
    print(fibonacci(i), end=" ")




def power(a, b):
    if b == 0:         
        return 1
    else:
        return a * power(a, b - 1)   


a = int(input("\n Enter base: "))
b = int(input("Enter exponent: "))

result = power(a, b)
print("Result:", result)
