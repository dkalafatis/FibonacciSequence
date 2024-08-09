def fibonacci_sequence(limit=None, position=None):
    sequence = [0, 1]
    if position:
        while len(sequence) < position:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence
    elif limit is not None:
        while sequence[-1] + sequence[-2] <= limit:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence


def main():
    choice = input(
        "Type 'number' to generate up to a certain number or 'position' to generate up to a certain position: ").strip().lower()

    if choice == 'number':
        try:
            number = int(input("Enter the number up to which you want the Fibonacci sequence generated: "))
            if number < 0:
                print("Please enter a positive integer.")
            else:
                result = fibonacci_sequence(limit=number)
                print(f"The Fibonacci sequence up to {number} is: {result}")
        except ValueError:
            print("Please enter a valid integer.")

    elif choice == 'position':
        try:
            position = int(input("Enter the position up to which you want the Fibonacci sequence generated: "))
            if position <= 0:
                print("Please enter a positive integer greater than 0.")
            else:
                result = fibonacci_sequence(position=position)
                print(f"The Fibonacci sequence up to position {position} is: {result}")
        except ValueError:
            print("Please enter a valid integer.")

    else:
        print("Invalid choice. Please type 'number' or 'position'.")


if __name__ == "__main__":
    main()
