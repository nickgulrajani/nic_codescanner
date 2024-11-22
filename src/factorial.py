def factorial_iterative(n):
    """
    Calculate factorial using iteration
    Args:
        n (int): Non-negative integer
    Returns:
        int: Factorial of n
    """
    # Check for negative input
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Handle special cases
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """
    Calculate factorial using recursion
    Args:
        n (int): Non-negative integer
    Returns:
        int: Factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Example usage
if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        print(f"Factorial (iterative) of {num} is: {factorial_iterative(num)}")
        print(f"Factorial (recursive) of {num} is: {factorial_recursive(num)}")
    except ValueError as e:
        print(f"Error: {e}")