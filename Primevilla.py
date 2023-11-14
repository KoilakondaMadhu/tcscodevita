# Primevilla
Marks: 30
# Problem Description
# It rains only on certain days in Primevilla. It is a rainy day when the number of days since a certain date is prime as well as the month is prime (i.e., month is one of Feb, Mar, May, Jul, Nov). Primevilla follows same calendar that we use.

# Given the date d, identify if it would ever rain on a given weekday w within the next given n days. Also calculate the number of days r (where r > 0) after which it would rain within the next n days.

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

# Constraints
# 2 <= n <= 10 ^ 10

# Input
# Input consists of three space delimited parts viz. <Date, DOW, n> where

# Date is of the format yyyymmdd
# DOW is Date of the Week in Ddd format
# n is a natural number (where n>=2)
# Output
# Output would be one of the three formats

# If it would rain on Ddd, r days after d within the next n days, print 'Yes r'
# Else if p is the least prime > n such that it would rain on Ddd after p days, print 'No p'
# Else print 'No 0', if it would never rain on Ddd.
# Time Limit (secs)
# 1

# Examples
# Example 1

# Input

# 20211201 Sun 100

# Output

# Yes 67

# Explanation

# Starting from 20211201 we start checking for prime number days whether it would rain. The process will be as depicted below

# 20211201+2 is 20211203 Fri, month 12 is not prime ---> It would not rain

# 20211201+3 20211204 Sat, month 12 is not prime ---> It would not rain

# ..

# 20211201+31 is 20220101 Sat, month 1 is not prime ---> It would not rain

# ..

# 20211201+67 is 20220206 Sun, month 2 is prime ---> It would rain

# Hence it could rain on a Sunday 67 days after the given date and within the given 100 days. Hence, output is "Yes 67"

# Example 2

# Input

# 20211201 Wed 100

# Output

# No 0

# Explanation

# The given date 20211201 is itself a Wednesday.

# 20211201+7 is 20211208 Wed, month 12 is not prime ---> It would not rain

# Also, any future Wednesday would be a multiple of 7 and hence non-prime days later than 20211201. So, it would never rain on future Wednesdays. Hence, output is "No 0"

# Example 3

# Input

# 19470815 Sat 150

# Output

# No 197

# Explanation

# If similar computation as depicted in prior examples is carried out one can figure out that it will rain on Sat, 28 Feb 1948 which is 197 days from 15 Aug 1947. However, since 197 is greater than 150 output is "No 197"
