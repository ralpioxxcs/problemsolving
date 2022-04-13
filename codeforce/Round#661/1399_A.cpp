#include <bits/stdc++.h>
#define TEST
using namespace std;
int main() {
  cin.tie(0)->sync_with_stdio(0);
  cout.tie(0);
#ifdef TEST
  freopen("input.txt", "r", stdin);
#endif
  int T;
  string ans;
  int n;  // (1<=n<=50)
  cin >> T;
  while (T--) {
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
      cin >> a[i];
    }
    sort(a.begin(), a.end());
    int min_val = 101;
    for (int i = 0; i < n - 1; i++) {
      if (abs(a[i] - a[i + 1]) <= 1) {
        continue;
      } else {
        cout << "NO\n";
        break;
      }
    }
    cout << "YES\n";
  }
  return 0;
}
