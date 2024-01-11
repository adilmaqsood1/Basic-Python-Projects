import operations

def main():
    try:
        # Input two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Display menu
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        
        # Input choice
        choice = int(input("Enter choice (1/2/3/4): "))
        
        # Perform operation based on user's choice
        if choice == 1:
            result = operations.addition(num1, num2)
        elif choice == 2:
            result = operations.subtraction(num1, num2)
        elif choice == 3:
            result = operations.multiplication(num1, num2)
        elif choice == 4:
            result = operations.division(num1, num2)
        else:
            print("Invalid choice")
            return  # Exit the program
        
        # Display the result
        print("Result:", result)
    
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()
