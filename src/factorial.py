def factorial_iterative(n):
    """
    Calculate factorial using iteration
    Args:
        n (int): Non-negative integer
    Returns:
        int: Factorial of n
    """
    print(f"\nCalculating {n}! using iterative method...")
    
    # Check for negative input
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Handle special cases
    if n == 0 or n == 1:
        print(f"Special case: {n}! = 1")
        return 1
    
    result = 1
    for i in range(2, n + 1):
        old_result = result
        result *= i
        print(f"Step {i-1}: {old_result} × {i} = {result}")
    
    print(f"Final result: {n}! = {result}")
    return result

def factorial_recursive(n):
    """
    Calculate factorial using recursion
    Args:
        n (int): Non-negative integer
    Returns:
        int: Factorial of n
    """
    print(f"Calculating factorial of {n}")
    
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        print(f"Base case: {n}! = 1")
        return 1
    
    result = n * factorial_recursive(n - 1)
    print(f"Returning: {n}! = {n} × {n-1}! = {result}")
    return result

# Example usage
if __name__ == "__main__":
    print("Welcome to Factorial Calculator!")
    print("--------------------------------")
    try:
        num = int(input("Enter a non-negative integer: "))
        print("\n=== Using Iterative Method ===")
        iter_result = factorial_iterative(num)
        
        print("\n=== Using Recursive Method ===")
        rec_result = factorial_recursive(num)
        
        print("\n=== Summary ===")
        print(f"Factorial of {num}:")
        print(f"- Iterative method: {iter_result}")
        print(f"- Recursive method: {rec_result}")
        
    except ValueError as e:
        print(f"Error: {e}")