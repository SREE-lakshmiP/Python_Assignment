
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


try:
    number = int(input("Enter a non-negative integer: "))
    if number < 0:
        print("Please enter a non-negative integer.")
    else:
        
        iterative_result = factorial_iterative(number)
        recursive_result = factorial_recursive(number)
        
        
        print(f"Factorial of {number} (iterative): {iterative_result}")
        print(f"Factorial of {number} (recursive): {recursive_result}")

except ValueError:
    print("Invalid input. Please enter a non-negative integer.")