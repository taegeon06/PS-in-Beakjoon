#include <bits/stdc++.h>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);                                                                           

	int a, b, c, d;

	cin >> a >> b >> c;
	cin >> d;

	if (c + d >= 60) {
		if ((c + d) % 60 == 0) {
			b += (c + d) / 60;
			c = 0;

		} else {
			b += (c + d) / 60;
			c = (c + d) % 60;
		}           

	} else {
		c += d;
	}

	if (b >= 60) {
		a += b / 60;
		b = b % 60;
	}
	
	if (a >= 24) {
		a = a % 24;
	}

	cout << a << " " << b << " " << c;
	return 0;
}