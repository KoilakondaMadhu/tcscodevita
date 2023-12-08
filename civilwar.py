# Get the total number of Avengers
N = int(input())

# Get the powers of each Avenger as a list
powers = list(map(int, input().split()))

# Initialize the power of Team A and Team B
team_a_power = 0
team_b_power = 0

# Sort the powers in descending order based on their absolute values,
# breaking ties by preferring negative values
powers.sort(key=lambda x: (abs(x), -x), reverse=True)

# Assign Avengers to teams alternatively (Ironman's turn)
ironman_turn = True

for power in powers:
    # Add the power to the corresponding team based on whose turn it is
    if ironman_turn:
        team_a_power += power
    else:
        team_b_power += power
    
    # Switch turns for the next iteration
    ironman_turn = not ironman_turn

# Calculate the absolute difference in power between Team A and Team B
power_difference = abs(team_a_power - team_b_power)

# Print the result
print(power_difference)




# TCS CodeVita 
# Civil War
# Problem Description
# In this superhero epic, the denizens of the Marvel Universe are forced to pick sides when Captain America and Iron Man come to blows over ideological differences.
# The government decides to push for the Hero Registration Act, a law that limits a hero’s actions. This results in a division in The Avengers. Iron Man stands with this Act, claiming that their actions must be kept in check otherwise cities will continue to be destroyed, but Captain America feels that saving the world is daring enough and that they cannot rely on the government to protect the world. And here the civil war begins.

# They are trying make their team stronger by adding more avengers to their team. There are N avengers lined up.

# Rules to add avenger to their team-

# Any team can start first. But they will alternatively only.
# They can select avenger from any side. But if they start from one side they can’t move to other side in current chance.
# They can select consecutive avengers as many they want.
# They will stop only when all the avengers are part of either side.
# Every Avenger has a power associated with him
# There are some spurious avengers who will decrease the overall power of the team.
# Both teams will select players optimally. Find the difference of powers of the two teams

# Constraints
# 1<= N <= 10^6
# -10^9 <= p[i] <= 10^9

# Input
# First line contains an integer denoting the number of Avengers(N).
# Next lines contain N space separated values denoting power of every avenger(P[i]).

# Output
# Print the difference of the powers of teams
# – Time Limit (secs)
# 1

# Examples :
# Input
# 5
# 2-78-1 20

# Output
# 2
