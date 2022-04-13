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
  int n;
  while (T--) {
    cin >> n;
    vector<long long> a(n);
    int ans = 0;
    for (long long i = 0; i < n; i++) {
      cin >> a[i];
    }
    // solve
    for(long long i=0; i<n;i++) {
      ans = n-1;
    }
    cout << ans << endl;
  }
  return 0;
}

