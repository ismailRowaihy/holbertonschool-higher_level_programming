#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
is_greater = 'greater then 5'if last_digit > 5 else('0' if last_digit == 0 else 'less then 6 and not 0')
print(f"Last digit of {number} is {last_digit if number > 0 else -last_digit} and is {is_greater}")
