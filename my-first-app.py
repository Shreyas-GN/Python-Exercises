#Time Converter-102 App
print("Welcome to the Age to Time Converter!")
print("This simple app converts your age in years to months, days, hours, and minutes.")
print("Let's get started!\n")
# Get user input for age
user_age = input("Enter your age: ")

# Validate if the input is numeric
if user_age.isdigit():
    age_number = int(user_age)
    
    # Calculate age in months, days, hours, and minutes
    months = age_number * 12
    days = age_number * 365
    hours = days * 24
    minutes = hours * 60

    # Display the result with additional details
    print(f"{age_number} years is equal to:")
    print(f"{months} months")
    print(f"{days} days")
    print(f"{hours} hours")
    print(f"{minutes} minutes")
else:
    print("Please enter a valid number for your age.")
