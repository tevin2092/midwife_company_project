from datetime import datetime

def get_correct_input(prompt, validate_func):
    while True:
        user_input = input(prompt)
        if validate_func(user_input):
            return user_input
        print("Invalid input. Please try again.")

def correct_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def correct_time(time_str):
    try:
        datetime.strptime(time_str, '%H:%M')
        return True
    except ValueError:
        return False
