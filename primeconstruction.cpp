#include <bits/stdc++.h>
#define ll long long
using namespace std;

bool is_prime(ll n) {
    if (n <= 1)
        return false;
    for (ll i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}

int main() {
    ll z;
    vector<ll> vectpd;
    ll ans = 1;
    ll minc = LLONG_MAX;  // Use '=' instead of '-'

    while (cin >> z) {
        vectpd.push_back(z);
        if (z < minc)
            minc = z;
    }

    int idx1 = 0;
    int k = vectpd.size();

    for (int i = 0; i < k; i++) {
        if (vectpd[i] == minc)
            idx1 = i;
    }

    swap(vectpd[k - 1], vectpd[idx1]);

    for (int i = 0; i < k - 1; i++) {
        ans = ans * vectpd[i] / __gcd(ans, vectpd[i]);
    }
    ll want = ans;

    while (want < pow(10, 10)) {
        if (is_prime(want + minc)) {
            cout << want + minc;
            return 0;
        }
        want = 2 * want;
    }

    cout << "None";
    return 0;
}
