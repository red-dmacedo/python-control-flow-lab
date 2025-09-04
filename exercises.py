# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    vowels = ['a', 'e', 'i', 'o', 'u']
    upper_vowels = [v.upper() for v in vowels]
    letter = input('Enter a letter: ')
    if len(letter) > 1 or len(letter) == 0:
        print("Only one letter is accepted")
    elif not letter.isalpha():
        print("You must enter an alphabetic value")
    elif letter in vowels or letter in upper_vowels:
        print(f"The letter {letter} is a vowel")
    else:
        print(f"The letter {letter} is a consonant")

# Call the function
check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    try: age = int(input('Please enter your age: '))
    except Exception as e:
        print(e)
        print("Error: Input must be an integer")
        return
    voting_age = 18
    if age < 0:
        print("Invalid input")
    elif age >= voting_age:
        print("You can vote!")
    elif age < voting_age:
        print("You are too young to vote.")

    # Call the function
check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    try: age = int(input("Input a dog's age: "))
    except Exception as e:
        print(e)
        print('Input must be an integer')
    if age > 2:
        age -= 2 # remove first 2 years
        age *= 7 # convert later years to dog years
        age += 20 # add back the first 2 years
    elif age >= 2:
        age *= 10 # calc age
    print(age)


# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    def convert_yes_no(s):
        if s.lower() in ["y", "yes"]:
            return True
        elif s.lower() in ["n", "no"]:
            return False
        else:
            raise Exception(f"Invalid input: {s}")
    iscold = convert_yes_no(input("Is it cold? [(y)es/(n)o]: "))
    israin = convert_yes_no(input("Is it raining? [(y)es/(n)o]: "))
    match f"{iscold}, {israin}":
        case "True, True":
            print("Wear a waterproof coat.")
        case "True, False":
            print("Wear a warm coat.")
        case "False, True":
            print("Carry an umbrella.")
        case "False, False":
            print("Wear light clothing.")


# Call the function
weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Your control flow logic goes here
    month_list = [
        "jan", "feb", "mar", "apr", "may", "jun",
        "jul", "aug", "sep", "oct", "nov", "dec"
    ]

    # additional check for maximum day of a month could be added, but was omitted
    seasons = [
        {
            "name": "winter",
            "start": {
                "month": month_list[-1],
                "day": 21,
            },
            "full_months": month_list[0:2],
            "end": {
                "month": month_list[2],
                "day": 19
            }
        },

        {
            "name": "spring",
            "start": {
                "month": month_list[2],
                "day": 20,
            },
            "full_months": month_list[3:5],
            "end": {
                "month": month_list[5],
                "day": 20
            }
        },

        {
            "name": "Summer",
            "start": {
                "month": month_list[5],
                "day": 21,
            },
            "full_months": month_list[6:8],
            "end": {
                "month": month_list[8],
                "day": 21
            }
        },

        {
            "name": "Fall",
            "start": {
                "month": month_list[8],
                "day": 22,
            },
            "full_months": month_list[9:11],
            "end": {
                "month": month_list[11],
                "day": 20
            }
        },
    ]
    month = (input("Enter the month of the year (Jan - Dec): ")).lower()
    if not month in month_list:
        raise Exception("Input must be the first 3 letters of a month")
    try:
        day = int(input("Enter the day of the month: "))
        if day < 1:
            raise Exception("Invalid input: day cannot be 0 or negative")
        if day > 33:
            raise Exception("Invalid input: day cannot be larger than 32")
    except Exception as e:
        print(e)
        return
    for season in seasons:
        if (month in season['full_months']) or \
                (month == season['start']['month'] and day >= season['start']['day']) or \
                (month == season['end']['month'] and day <= season['end']['day']):
            print(f"{month} {day} is in {season['name']}")

        # Call the function
determine_season()
