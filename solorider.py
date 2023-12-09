import sys

def calculate_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def min_distance_traveled(N, M, passengers, vehicles):
    passengers.sort()  # Sort passengers lexicographically

    total_distance = 0
    assigned_vehicles = set()

    for passenger in passengers:
        passenger_name, passenger_location = passenger

        min_distance = sys.maxsize
        selected_vehicle = ""

        for vehicle in vehicles:
            vehicle_name, vehicle_location = vehicle

            if vehicle_name not in assigned_vehicles:
                distance = calculate_distance(passenger_location, vehicle_location)

                if distance < min_distance or (distance == min_distance and vehicle_name < selected_vehicle):
                    min_distance = distance
                    selected_vehicle = vehicle_name

        total_distance += min_distance
        assigned_vehicles.add(selected_vehicle)

    return total_distance

# Input
N, M = map(int, input().split())

passengers = []
for _ in range(N):
    name, x, y = input().split()
    passengers.append((name, (int(x), int(y))))

vehicles = []
for _ in range(M):
    name, x, y = input().split()
    vehicles.append((name, (int(x), int(y))))

# Output
result = min_distance_traveled(N, M, passengers, vehicles)
print(result)
