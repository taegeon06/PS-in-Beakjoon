#include <bits/stdc++.h>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
                      
    int t, a, b;

    cin >> t;

    for (int i = 1; i < t + 1; i++) {
    	cin >> a >> b;
    	cout << "Case #" << i << ": " << a + b << "\n";
    }
	return 0;	
}