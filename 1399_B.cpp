#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


// test case, number of gifts
int t, n; 
// nubmer of candy, orange, each contains
std::vector<int> a;
std::vector<int> b;
// 
int min_a, min_b;
int res;

////////////////////////////////////////////////////////

void output() {
	std::cout << "A : " << std::endl;
	for (auto &v : a) {
		std::cout << v << ",";
	}
	std::cout << " " << std::endl;
	std::cout << "B : " << std::endl;
	for (auto &v : b) {
		std::cout << v << ",";
	}
	std::cout << " " << std::endl << std::endl;
}

void solve() {
	int count = 0;
	int i = 0;

	while (i!=n) {

		// both eat A,B
		if (min_a < a[i] && min_b < b[i]) {
			--a[i];
			--b[i];			
		}
		// only eat A
		else if (min_a < a[i] && min_b >= b[i]) {
			--a[i];		
		}
		else if (min_a >= a[i] && min_b < b[i]) {
			--b[i];
		}
		else {
			i += 1;
			continue;
		}
		count += 1;
		output();
	}
	res = count;
}

int main() {
	// input
	freopen("input.txt", "r", stdin);

	std::cin >> t;
	while (--t) {
		std::cin >> n;
		a.resize(n, 1000000001);
		b.resize(n, 1000000001);
		for (int s = 0; s < n; s++) {
			std::cin >> a[s];
		}
		for (int s = 0; s < n; s++) {
			std::cin >> b[s];
		}
		min_a = *min_element(a.begin(), a.end());
		min_b = *min_element(b.begin(), b.end());

		solve();
		std::cout << res << std::endl;
	}
	return 0;
}