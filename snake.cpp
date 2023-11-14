#include <iostream>
#include <map>

// Constants for directions
const char NORTH = 'N';
const char SOUTH = 'S';
const char EAST = 'E';
const char WEST = 'W';

bool isValidPosition(int x, int y, int N) {
    return 0 <= x && x < N && 0 <= y && y < N;
}

pair<int, int> moveSnake(int x, int y, char direction, int N) {
    if (direction == NORTH) {
        return {x, (y - 1 + N) % N};
    } else if (direction == SOUTH) {
        return {x, (y + 1) % N};
    } else if (direction == EAST) {
        return {(x + 1) % N, y};
    } else if (direction == WEST) {
        return {(x - 1 + N) % N, y};
    }
    // Invalid direction
    return {x, y};
}

bool isSnakePresent(int x, int y, const map<string, pair<pair<int, int>, pair<int, int>>>& snakes) {
    for (const auto& entry : snakes) {
        const auto& start_block = entry.second.first;
        const auto& end_block = entry.second.second;
        if (start_block.first <= x && x < end_block.first && start_block.second <= y && y < end_block.second) {
            cout << entry.first << " " << x + 1 << "," << y + 1 << endl;
            return true;
        }
    }
    return false;
}

int main() {
    int N, M;
    cin >> N >> M;

    map<string, pair<pair<int, int>, pair<int, int>>> snakes;

    for (int i = 0; i < M; i++) {
        string snake_name;
        cin >> snake_name;
        int x1, y1, x2, y2;
        char comma;
        cin >> x1 >> comma >> y1 >> x2 >> comma >> y2;
        snakes[snake_name] = {{x1, y1}, {x2, y2}};
    }

    string priest_start;
    cin >> priest_start;
    char direction = toupper(priest_start[0]);
    int number = stoi(priest_start.substr(1));

    int x = 0, y = 0;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < number; j++) {
            if (isSnakePresent(x, y, snakes)) {
                return 0;
            }
            auto new_position = moveSnake(x, y, direction, N);
            x = new_position.first;
            y = new_position.second;
        }
    }

    cout << "NIRVANA";
    return 0;
}
