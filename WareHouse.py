# Problem Description
# A godown, which in other words called as a warehouse, is a building which is used to store raw materials or manufactured goods until they are exported to other places.

# There are n number of go-downs which are used to store and ripe large quantity of bananas. Once the bananas are ripened, every godown owner will pack all those bananas as a single unit and transport them to airport for exporting them to other countries. All these godowns are close to each other and the owners are friendly. So while transporting the bananas, they would like to share the vehicle (if possible) in order to reduce the transportation cost. But only two people can share a vehicle and each vehicle can carry a weight of "w" tons at a time.

# Given an array representing the weights of bananas of each owner, the maximum limit that the vehicle can hold, find the minimum number vehicles needed to transport all the bananas to the airport.

# Note: There are no loads which are heavier than the given limit.

# The weight of the bananas is measured in tons.

# Constraints
# 0 <= len(arr) <= 10^5

# 0 <= arr[i] <= 10^5

# The array may have duplicate numbers.

# Input
# First line consists of an array of integers denoting the weights of bananas in the godown.

# Second line consists of a single integer k which denotes the maximum weight limit of the vehicle in tons.

# Output
# Print the minimum number of vehicles needed.

# Time Limit (secs)
# 1

# Examples
# Example 1

# Input

# 4 2 8 5 1 3 6

# 8

# Output

# 4

# Explanation

# We can load (8), (4,3), (6,2), (5, 1) in 4 different vehicles. Any other arrangements will never give less than 4 vehicles.

# Example 2

# Input

# 4 7 9 11 6 8 3

# 12

# Output

# 5

# Explanation

# We can load (11), (8,3), (6,4), (9), (7) in 5 different vehicles. Any other arrangements will never give less than 5 vehicles.

def minimum_vehicles(weights, max_limit):
    
    sorted_weights = sorted(filter(lambda x: x != 0, weights), reverse=True)
    
    left, right = 0, len(sorted_weights) - 1
    vehicles = 0
        
    while left <= right:
        if sorted_weights[left] + sorted_weights[right] <= max_limit:
            right -= 1
        left += 1
        vehicles += 1

    return vehicles

weights = list(map(int, input().split()))
max_limit = int(input())

result = minimum_vehicles(weights, max_limit)
print(result,end="")
