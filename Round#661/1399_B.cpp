#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
// test case, number of gifts
int t;
long long n;
// nubmer of candy, orange, each contains
std::vector<long long> a;
std::vector<long long> b;
long long min_a, min_b;
long long res;

////////////////////////////////////////////////////////

long long solve() {
  long long count = 0;
  for (int i = 0; i < n; i++) {
    count += max(a[i] - min_a, b[i] - min_b);
  }
  return count;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  cout.tie(0);
  std::cin >> t;
  while (t--) {
    std::cin >> n;
    min_a = 1e9;
    min_b = 1e9;
    a.resize(n, 1e9);
    b.resize(n, 1e9);
    for (int s = 0; s < n; s++) {
      std::cin >> a[s];
      min_a = min(min_a, a[s]);
    }
    for (int s = 0; s < n; s++) {
      std::cin >> b[s];
      min_b = min(min_b, b[s]);
    }
    long long ans = solve();
    std::cout << ans << "\n";
  }
  return 0;
}