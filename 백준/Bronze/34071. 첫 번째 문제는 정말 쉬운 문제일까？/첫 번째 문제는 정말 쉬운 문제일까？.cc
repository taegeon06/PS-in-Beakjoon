#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    int mn = int(1e9), mval = 0, val = 0;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;

        if (i == 0) val = x;

        mn = min(mn, x);
        mval = max(mval, x);
    }

    if (mn == val) cout << "ez" << '\n';
    else if (mval == val) cout << "hard" << '\n';
    else cout << '?' << '\n';
    return 0;
}