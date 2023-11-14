#include<bits/stdc++.h>
using namespace std;

int main() {
    int m1, m2, N;
    cin >> m1 >> m2 >> N;

    // Vector to store populations
    vector<int> populations;

    // Input populations until there is no more input
    while (true) {
        int t;
        cin >> t;

        // Break the loop when there is no more input
        if (cin.eof())
            break;

        populations.push_back(t);
    }

    // Sort populations in descending order
    sort(populations.begin(), populations.end(), greater<int>());

    int time1 = 0, time2 = 0;

    // Use size_t for the loop variable to avoid the warning
    for (size_t i = 0; i < populations.size(); i++) {
        if (time1 <= time2)
            time1 += populations[i] * m1;
        else
            time2 += populations[i] * m2;
    }

    int ans = max(time1, time2);
    cout << ans << " ";  // Ensure there is exactly one space after the output value

    return 0;
}
