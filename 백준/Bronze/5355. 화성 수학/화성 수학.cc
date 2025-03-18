#include <bits/stdc++.h>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	int t;
	float a;
	string tm;

	cin >> t;

	for (int i = 0; i < t; i++) {
		cin >> a;
		getline(cin, tm);		

		for (int i = 0; i < tm.size(); i++) {

//			cout << a << " " << tm << "\n";

			if (tm[i] == '@') {
				a *= 3;
			}

			if (tm[i] == '%') {
				a += 5;
			}

			if (tm[i] == '#') {
				a -= 7;
			}
		}
		
		cout << fixed;
		cout.precision(2);
		cout << a << "\n";
	}

	
	return 0;	
}