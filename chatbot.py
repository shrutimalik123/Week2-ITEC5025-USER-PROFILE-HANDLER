"""
Week 2 Assignment: Building a Chatbot's User Profile Handler
Author: Shruti Malik
Course: ITEC 5025
Date: 2026-01-21

Description:
This script implements a basic chatbot that:
1. Greets the user.
2. Handles user input with type conversion.
3. Performs arithmetic calculations.
4. Performs comparisons.
5. Uses logical operators for conditional responses.
"""

def greet_user():
    """
    Greets the user and introduces the chatbot's purpose.
    """
    print("Chatbot: Hello! I am your generic assistance chatbot.")
    print("Chatbot: I can help you with basic calculations, comparisons, and simple profile questions.")
    print("Chatbot: How can I assist you today?")

def get_user_profile():
    """
    Collects user profile information to demonstrate variable types and conversion.
    Returns a dictionary with user profile data.
    """
    print("\n--- User Profile Setup ---")
    
    # String variable
    name = input("Chatbot: What is your name? ")
    
    # Integer variable with type conversion and error handling
    age = 0
    try:
        age_input = input(f"Chatbot: Hi {name}, how old are you? ")
        age = int(age_input)
    except ValueError:
        print("Chatbot: That doesn't look like a valid number for age. Defaulting to 0.")
        age = 0
        
    # Float variable with type conversion
    height = 0.0
    try:
        height_input = input("Chatbot: How tall are you (in meters)? ")
        height = float(height_input)
    except ValueError:
        print("Chatbot: Invalid height format. Defaulting to 0.0.")
        height = 0.0
        
    # Boolean variable
    is_student_input = input("Chatbot: Are you currently a student? (yes/no): ").lower()
    is_student = True if is_student_input == 'yes' else False
    
    print(f"Chatbot: Profile saved. Name: {name}, Age: {age}, Height: {height}m, Student: {is_student}")
    
    return {"name": name, "age": age, "height": height, "is_student": is_student}

def perform_arithmetic():
    """
    Demonstrates arithmetic operators: +, -, *, /
    """
    print("\n--- Arithmetic Operations ---")
    print("Chatbot: I can perform simple calculations.")
    
    try:
        num1 = float(input("Chatbot: Enter the first number: "))
        num2 = float(input("Chatbot: Enter the second number: "))
        
        operation = input("Chatbot: Choose an operation (+, -, *, /): ")
        
        result = 0
        if operation == "+":
            result = num1 + num2
            print(f"Chatbot: {num1} + {num2} = {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"Chatbot: {num1} - {num2} = {result}")
        elif operation == "*":
            result = num1 * num2
            print(f"Chatbot: {num1} * {num2} = {result}")
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
                print(f"Chatbot: {num1} / {num2} = {result}")
            else:
                print("Chatbot: Error. Cannot divide by zero.")
        else:
            print("Chatbot: Unknown operation.")
            
    except ValueError:
        print("Chatbot: Please enter valid numbers.")

def perform_comparison():
    """
    Demonstrates comparison operators: ==, !=, <, >
    """
    print("\n--- Comparison Operations ---")
    print("Chatbot: I can compare two numbers for you.")
    
    try:
        val1 = float(input("Chatbot: Enter the first value to compare: "))
        val2 = float(input("Chatbot: Enter the second value to compare: "))
        
        if val1 == val2:
            print(f"Chatbot: {val1} is equal to {val2}.")
        else:
            print(f"Chatbot: {val1} is NOT equal to {val2}.")
            
        if val1 > val2:
            print(f"Chatbot: {val1} is greater than {val2}.")
        elif val1 < val2:
            print(f"Chatbot: {val1} is less than {val2}.")
            
    except ValueError:
        print("Chatbot: Invalid input for comparison.")

def check_logic(profile):
    """
    Demonstrates logical operators: and, or, not
    Uses the user profile content for context.
    """
    print("\n--- Logical Operations ---")
    print("Chatbot: Checking product recommendations based on your profile...")
    
    age = profile.get("age", 0)
    is_student = profile.get("is_student", False)
    
    # Example: Product for students OR people under 25
    if is_student or age < 25:
        print("Chatbot: You qualify for our 'Youth & Student' discount! (Reason: Student OR Under 25)")
    else:
        print("Chatbot: You do not qualify for the 'Youth & Student' discount.")
        
    # Example: Product for adults AND non-students (e.g. full price professional plan)
    if age >= 18 and not is_student:
        print("Chatbot: We recommend our 'Professional' plan for you. (Reason: Adult AND Not a Student)")
        
    # Example: NOT operator
    if not (age < 18):
        print("Chatbot: You are eligible to view adult categories. (Reason: NOT under 18)")

def main():
    """
    Main function to run the chatbot flow.
    """
    greet_user()
    
    # 1. Collect User Input & Handle Types
    user_profile = get_user_profile()
    
    # 2. Arithmetic
    perform_arithmetic()
    
    # 3. Comparison
    perform_comparison()
    
    # 4. Logical
    check_logic(user_profile)
    
    print("\nChatbot: It was nice talking to you! Goodbye.")

if __name__ == "__main__":
    main()
