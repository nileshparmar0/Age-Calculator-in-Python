from datetime import date

def calculate_age(birthday):
    today = date.today()  # Get today's date

    # Check if the birthdate is in the future
    if today < birthday:
        return "Invalid birthdate. Please enter a valid date."

    # Check if the birthday has occurred yet this year
    day_check = (today.month, today.day) < (birthday.month, birthday.day)
    # Calculate the difference in years
    year_diff = today.year - birthday.year - day_check
    # Calculate the remaining months until the next birthday
    remaining_months = (today.month - birthday.month - (today.day < birthday.day)) % 12
    # Calculate the remaining days until the next birthday
    remaining_days = (today - date(today.year, today.month, birthday.day)).days % 30

    # Return the age as a formatted string
    age_string = f"Age: {year_diff} years, {remaining_months} months, and {remaining_days} days"
    return age_string

if __name__ == "__main__":
    print("Age Calculator By Python")

    try:
        # Prompt the user to enter the birth year, month, and day
        birthYear = int(input("Enter the birth year: "))
        birthMonth = int(input("Enter the birth month: "))
        birthDay = int(input("Enter the birth day: "))
        # Create a date object for the birthdate
        dateOfBirth = date(birthYear, birthMonth, birthDay)
        # Calculate the age based on the birthdate
        age = calculate_age(dateOfBirth)
        # Print the calculated age
        print(age)
    except ValueError:
        # Handle cases where the user inputs non-integer values
        print("Invalid input. Please enter valid integers for the year, month, and day.")
