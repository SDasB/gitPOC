import time
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 40 # You can adjust the value of n as needed
start_time = time.time()

result = fibonacci(n)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"The12333 {n}-th Fibonacci number is: {result}")
print(f"Elapsed time: {elapsed_time} seconds")