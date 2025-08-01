#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;

    vector<int> a(n), tm(n);
    map<int, int> val;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        tm[i] = a[i];

        val[a[i]] = i;
    }

    sort(tm.begin(), tm.end());

    int ans = 0;
    for (int i = 0; i < n; i++) {
        if (tm[i] != a[i]) {
            int j = val[tm[i]];
            ans++;
            swap(a[i], a[j]);
            swap(val[a[i]], val[a[j]]);
        }
    }

    cout << ans;
    return 0;
}