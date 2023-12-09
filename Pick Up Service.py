from collections import defaultdict

def pick_up_service(num_cities, starting_city, connections, cache={}):
    if starting_city in cache:
        return cache[starting_city]

    graph = defaultdict(list)
    taxes = defaultdict(int)

    for i in range(num_cities - 1):
        city1, city2, goods, tax = connections[i]
        graph[city1].append((-1 * goods, tax, city2))
        taxes[city2] = tax

    route = []

    def dfs(city):
        route.append(city)
        for neighbor in sorted(graph[city]):
            dfs(neighbor[2])
            route.append(city)

    dfs(starting_city)
    total_tax = 0
    for c in route[1:]:
        total_tax += taxes[c]

    result = route, total_tax
    cache[starting_city] = result
    return result

num_cities = int(input())

connections_list = []

for _ in range(num_cities - 1):
    line = input()
    line_split = line.split()
    connections_list.append((line_split[0], line_split[1], int(line_split[2]), int(line_split[3])))

result_route, result_total_tax = pick_up_service(num_cities, connections_list[0][0], connections_list)

print("-".join(result_route))
print(result_total_tax, end="")
