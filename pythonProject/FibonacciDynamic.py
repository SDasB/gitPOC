import time
def fibonacci_dynamic(n, memo={}):
    if n <= 1:
        return n

    # Check if the result for 'n' is already in the memo dictionary
    if n not in memo:
        # If not, calculate and store the result in the memo dictionary
        memo[n] = fibonacci_dynamic(n - 1, memo) + fibonacci_dynamic(n - 2, memo)

    return memo[n]


# Example usage
n = 40
start_time = time.time()

result = fibonacci_dynamic(n)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"The {n}-th Fibonacci number is: {result}")
print(f"Elapsed time: {elapsed_time} seconds")