#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    ll n, q;
    cin >> n >> q;
    vector<pair<ll, ll>> a(n);
    vector<ll> tm(n);
    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        a[i] = {y, x};
        tm[i] = y;
    }

    sort(a.begin(), a.end(), [](pair<ll, ll> x, pair<ll, ll> y) {
        return x.first < y.first;
    });
    sort(tm.begin(), tm.end());

    vector<ll> pf1(n), pf2(n);
    for (int i = 0; i < n; i++) {
        pf1[i] = (ll(1e9) - a[i].first) * a[i].second;
        pf2[i] = (a[i].first - ll(-1e9)) * a[i].second;
    }

    for (int i = 1; i < n; i++) pf1[i] += pf1[i - 1];
    for (int i = n - 2; i > -1; i--) pf2[i] += pf2[i + 1];

    vector<ll> pf3(n), pf4(n);
    for (int i = 0; i < n; i++) {
        pf3[i] = a[i].second;
        pf4[i] = a[i].second;
    }

    for (int i = 1; i < n; i++) pf3[i] += pf3[i - 1];
    for (int i = n - 2; i > -1; i--) pf4[i] += pf4[i + 1];

    for (int i = 0; i < q; i++) {
        ll x;
        cin >> x;

        auto k = lower_bound(tm.begin(), tm.end(), x) - tm.begin();

        // if (k == n) cerr << k << '\n';
        // else cerr << x << " " << tm[k] << " " << i + 1 << '\n';

        if (k == 0) {
            if (x < tm[k]) {
                cout << pf2[0] - pf4[0] * (x - ll(-1e9)) << '\n';
            } else {
                cout << pf2[1] - pf4[1] * (x - ll(-1e9)) << '\n';
            } 
            continue;
        }

        if (k == n) {
            cout << pf1[n - 1] - pf3[n - 1] * (ll(1e9) - x) << '\n';
            continue;
        }


        if (k == n - 1) {
            if (x < tm[k]) {
                cout << pf2[k] - pf4[k] * (x - ll(-1e9)) + pf1[k - 1] - pf3[k - 1] * (ll(1e9) - x) << '\n';
            } else {
                cout << pf1[n - 2] - pf3[n - 2] * (ll(1e9) - x) << '\n';
            }
            continue;    
        }

        if (x < tm[k]) {
            cout << pf2[k] - pf4[k] * (x - ll(-1e9)) + pf1[k - 1] - pf3[k - 1] * (ll(1e9) - x) << '\n';
        } else {
            cout << pf2[k + 1] - pf4[k + 1] * (x - ll(-1e9)) + pf1[k - 1] - pf3[k - 1] * (ll(1e9) - x) << '\n';
        }
    }
    return 0;
}