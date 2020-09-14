#include <bits/stdc++.h>
#include <iostream>
#define TEST

using namespace std;

int main() {
  cin.tie(0)->sync_with_stdio(0);
  cout.tie(0);
#ifdef TEST
  freopen("input.txt", "r", stdin);
#endif
  int T;
  int ans = 0;
  cin >> T;  // test case
  while (T--) {
    int n;
    cin >> n;  // number of participants
    vector<int> w(n);
    int minimum = 50, maximum = 0;
    for (int idx = 0; idx < n; idx++) {
      cin >> w[idx];  // weight of the i-th participants
      minimum = min(minimum, w[idx]);
      maximum = max(maximum, w[idx]);
    }
    // solve
    ans = 0;
    for (int opt = minimum; opt <= maximum * 2; opt++) {
      vector<bool> visit(n);
      int count = 0;
      for (int i = 0; i < n; i++) {
        if (!visit[i]) {
          for (int j = i + 1; j < n; j++) {
            if (!visit[j]) {
              if (w[i] + w[j] == opt) {
                visit[i] = visit[j] = true;
                count++;
                break;
              } else {
                continue;
              }
            } else {
              continue;
            }
          }
        } else {
          continue;
        }
      }
      ans = max(ans,count);
    }

    // ans
    cout << ans << endl;
  }
  return 0;
}
