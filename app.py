
#function to add numbers
def add_numbers(num1, num2):
    return num1 + num2



#function to checking if number is even
def is_even(number):
    return number % 2 == 0



#function to reverse a string
def reverse_string(text):
    return text[::-1]



#function to count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)



#function to calculate factorial
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial



#function applying decorator
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

@decorator_func
def apply_decorator(func):
    return func()



#sequences
def sort_by_age(people):
    return sorted(people, key=lambda person: person[1])



#set and dictionaries
def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged


#Object-Oriented Programming class creation
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")
