#include <bits/stdc++.h>
#define TEST
using namespace std;
int main() {
  cin.tie(0)->sync_with_stdio(0);
  cout.tie(0);
#ifdef TEST
  freopen("input.txt", "r", stdin);
#endif
  int n, q;  // n : amounts of plank, q : number of events
  cin >> n;
  vector<int> lop(10001);
  vector<int> sums(10001);
  int val;
  for (int i = 0; i < n; ++i) {
    cin >> val;
    lop[val]++;
    sums[lop[val]]++;
    sums[lop[val]-1]--;
  }
  cin >> q;  // number of events
  vector<int> ev(q);
  for (int i = 0; i < q; ++i) {
    char s;
    cin >> s;
    if (s == '+')
      cin >> ev[i];
    else if (s == '-') {
      cin >> ev[i];
      ev[i] = -ev[i];
    }
  }

  // solve ( q: 10^5 )
  for (int i = 0; i < q; ++i) {
    if (ev[i] > 0) {
      lop[abs(ev[i])]++;
      sums[lop[abs(ev[i])]]++;
      sums[lop[abs(ev[i])]-1]--;
    } else {
      sums[lop[abs(ev[i])]]--;
      lop[abs(ev[i])]--;
      sums[lop[abs(ev[i])]]++;
    }

    for (int i = 1; i <= 8; ++i) {
      std::cout << "ary ["<<i<<"] : "<<sums[i] << std::endl;
      
    }
    if ((sums[8] >= 1) || (sums[6] >= 1 && sums[2] >= 1) || (sums[4] >= 2) ||
        (sums[4] >= 1 && sums[2] >= 2)) {
      std::cout << "YES" << std::endl;
    } else {
      std::cout << "NO" << std::endl;
    }
  }
  return 0;
}

