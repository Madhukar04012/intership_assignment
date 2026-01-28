import random
import datetime
import os
import sys

# Checking for numpy
try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install it using 'pip install numpy'")
    # We will not exit here to allow other tasks to run if numpy is missing, 
    # but Task 2 will fail or we can handle it gracefully.
    np = None

def task1_operators():
    print("\n--- Task 1: Python Basics & Operators ---")
    try:
        # Taking inputs
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Arithmetic operations
    print(f"Addition: {num1} + {num2} = {num1 + num2}")
    print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
    print(f"Multiplication: {num1} * {num2} = {num1 * num2}")

    # Safe division and modulus
    if num2 != 0:
        print(f"Division: {num1} / {num2} = {num1 / num2}")
        print(f"Modulus: {num1} % {num2} = {num1 % num2}")
    else:
        print("Division: Cannot divide by zero!")
        print("Modulus: Cannot modulo by zero!")

    # Comparison operators
    print(f"{num1} > {num2}: {num1 > num2}")
    print(f"{num1} < {num2}: {num1 < num2}")
    print(f"{num1} == {num2}: {num1 == num2}")

    # Logical operators demonstration
    print(f"Both numbers > 0: {num1 > 0 and num2 > 0}")
    print(f"Either number > 0: {num1 > 0 or num2 > 0}")

def task2_lists_numpy():
    print("\n--- Task 2: Lists & NumPy ---")
    if np is None:
        print("Error: NumPy is not installed. Skipping NumPy part of the task.")
        return

    # Generate a list of 10 random integers
    numbers = [random.randint(1, 100) for _ in range(10)]
    print(f"Original List: {numbers}")

    # Add a value
    new_val = random.randint(1, 100)
    numbers.append(new_val)
    print(f"After appending {new_val}: {numbers}")

    # Remove the first element safely using pop
    if numbers:
        removed = numbers.pop(0)
        print(f"Removed first element ({removed}): {numbers}")
    
    # Find max and min
    print(f"Max value: {max(numbers)}")
    print(f"Min value: {min(numbers)}")

    # Sort the list
    numbers.sort()
    print(f"Sorted List: {numbers}")

    # Convert to NumPy array
    arr = np.array(numbers)
    print(f"NumPy Array: {arr}")
    
    # Calculate statistics
    print(f"Mean: {np.mean(arr):.2f}")
    print(f"Median: {np.median(arr):.2f}")
    print(f"Standard Deviation: {np.std(arr):.2f}")

def task3_dictionaries_sets():
    print("\n--- Task 3: Dictionaries & Sets ---")
    # Dictionary creation
    student = {
        "name": "Arjun",
        "course": "B.Tech CS",
        "marks": 82
    }

    # Assign grade using if-elif-else
    marks = student["marks"]
    if marks >= 90:
        student["grade"] = "A"
    elif marks >= 75:
        student["grade"] = "B"
    elif marks >= 60:
        student["grade"] = "C"
    else:
        student["grade"] = "D"

    # Print all key-value pairs
    print("Student Details:")
    for key, value in student.items():
        print(f"{key.capitalize()}: {value}")

    # Sets logic
    ai_tools_1 = {"ChatGPT", "Claude", "Gemini"}
    ai_tools_2 = {"Gemini", "Copilot", "Llama"}

    print(f"\nSet 1: {ai_tools_1}")
    print(f"Set 2: {ai_tools_2}")
    
    # Union and Intersection
    print(f"Union (All tools): {ai_tools_1.union(ai_tools_2)}")
    print(f"Intersection (Common tools): {ai_tools_1.intersection(ai_tools_2)}")

def task4_file_handling():
    print("\n--- Task 4: File Handling ---")
    filename = "ai_students.txt"
    
    # Create and write to file
    students_data = [
        "Amit,85,A",
        "Priya,72,C",
        "Rohan,90,A",
        "Sneha,78,B",
        "Vikram,65,C"
    ]
    
    with open(filename, "w") as f:
        for student in students_data:
            f.write(student + "\n")
    
    print(f"File '{filename}' created successfully.")

    print("\nReading file... Students with marks > 75:")
    try:
        with open(filename, "r") as f:
            for line in f:
                # Clean and parse the line
                parts = line.strip().split(',')
                if len(parts) == 3:
                    name, marks, grade = parts
                    # Convert marks to integer for comparison
                    if int(marks) > 75:
                        print(f"Name: {name}, Marks: {marks}, Grade: {grade}")
    except FileNotFoundError:
        print("Error: File not found.")

def task5_mini_project():
    print("\n--- Task 5: Real-World Mini Project (Prompt Logger) ---")
    
    # Get user prompt
    user_prompt = input("Enter your AI prompt: ")
    
    # Attach date and time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {user_prompt}\n"
    
    # Append to file
    filename = "prompt_history.txt"
    try:
        with open(filename, "a") as f:
            f.write(log_entry)
        print(f"Success: Prompt logged to '{filename}'")
    except Exception as e:
        print(f"Error logging prompt: {e}")

def main():
    while True:
        print("\n" + "="*40)
        print("   INTERNSHIP ASSIGNMENT - PYTHON FUNDAMENTALS")
        print("="*40)
        print("1. Task 1: Basics & Operators")
        print("2. Task 2: Lists & NumPy")
        print("3. Task 3: Dictionaries & Sets")
        print("4. Task 4: File Handling")
        print("5. Task 5: AI Prompt Logger (Mini Project)")
        print("6. Exit")
        print("="*40)
        
        choice = input("Select an option (1-6): ")
        
        if choice == '1':
            task1_operators()
        elif choice == '2':
            task2_lists_numpy()
        elif choice == '3':
            task3_dictionaries_sets()
        elif choice == '4':
            task4_file_handling()
        elif choice == '5':
            task5_mini_project()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
