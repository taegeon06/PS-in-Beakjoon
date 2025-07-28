#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    cin >> n >> m;
    vector<ll> a(n, 0);
    for (int i = 0; i < n; i++) cin >> a[i];

    for (int i = 0; i < m; i++) {
        ll s = 0, e;
        cin >> e;
        // cerr << e << '\n';

        for (int j = 0; j < n; j++) {
            if (s >= e) break;

            if (a[j] > s) {
                if (a[j] < e) {
                    ll tm = s;
                    s = a[j];
                    a[j] += a[j] - tm;   
                } else {
                    a[j] += (e - s);
                    break;
                }
            }
        }
    }

    for (auto x : a) cout << x << '\n';
    return 0;
}