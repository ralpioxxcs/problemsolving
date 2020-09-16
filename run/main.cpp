#include <bits/stdc++.h>
#define TEST
using namespace std;
int main() {
  cin.tie(0)->sync_with_stdio(0);
  cout.tie(0);
#ifdef TEST
  freopen("input.txt", "r", stdin);
#endif
  int n, q;    // n : amounts of plank, q : number of events
  int sl = 0;  // sum of length
  int count = 0;
  cin >> n;
  vector<int> lop(10001);
  int val;
  for (int i = 0; i < n; ++i) {
    cin >> val;
    if (lop[val] == 0) {
      count++;
    }
    lop[val]++;
    sl++;
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
    if (lop[abs(ev[i])] == 0) {
      count++;
    }
    if (ev[i] > 0) {
      lop[abs(ev[i])]++;
      sl++;
    } else {
      lop[abs(ev[i])]--;
      sl--;
    }
    std::cout << "sl"<<sl << std::endl;
    std::cout << "cur "<<lop[abs(ev[i])]<< std::endl;
    if (((count * 4) % sl) == 0)
      std::cout << "YES" << std::endl;
    else if (((sl - lop[abs(ev[i])]) % 8) == 0)
      std::cout << "YES" << std::endl;
    else
      std::cout << "NO" << std::endl;
  }
  return 0;
}

