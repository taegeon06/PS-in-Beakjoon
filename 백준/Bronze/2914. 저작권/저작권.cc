#include <bits/stdc++.h>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	float a, b, i;

	cin >> a >> i;
	b = 1;

	while (ceil(b / a) < i) {
		b++;
	}

	cout << b;
	return 0;	
}