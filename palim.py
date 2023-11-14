from datetime import timedelta as t
from datetime import datetime as d

# Function to generate a list of prime numbers up to a given limit
def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Input: Date, Day of the week, and a number h
dye, dwk, h = input().split()
h = int(h)

# List to store prime numbers
primes = generate_primes(365)

# Dictionary to map weekday index to its name
weekday_dict = {0: "Mon", 1: "Tue", 2: "Wed", 3: "Thu", 4: "Fri", 5: "Sat", 6: "Sun"}

# Convert the input date to a datetime object
dye = d.strptime(dye, "%Y%m%d")

# Initialize das (result) to -1
das = -1

# Check each prime number
for num in primes:
    # Calculate the date after adding the current prime number
    date_after_prime = dye + t(num)
    
    # Check if the month of the new date is prime and the weekday matches the input
    if is_prime(date_after_prime.month) and weekday_dict[date_after_prime.weekday()] == dwk:
        das = num
        break

# Output the result based on the conditions
if das == -1:
    print("No", 0, end="")
elif das <= h:
    print("Yes", das, end="")
else:
    print("No", das, end="")
