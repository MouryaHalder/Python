def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  # Initialize the sequence with the first two Fibonacci numbers

    # Generate the Fibonacci sequence up to the nth term
    for i in range(2, n):
        next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

def main():
    # Taking input from the user
    num_terms = int(input("Enter the number of Fibonacci terms to generate: "))

    # Generate the Fibonacci sequence
    fibonacci_sequence = generate_fibonacci(num_terms)

    # Displaying the Fibonacci sequence
    print("Fibonacci sequence:")
    for num in fibonacci_sequence:
        print(num, end=" ")

if __name__ == "__main__":
    main()
