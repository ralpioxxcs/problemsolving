#include <bits/stdc++.h>
#define TEST
#define ll long long
using namespace std;
int main() {
  cin.tie(0)->sync_with_stdio(0);
  cout.tie(0);
#ifdef TEST
  freopen("input.txt", "r", stdin);
#endif
  int T;
  ll x;
  cin >> T;
  while (T--) {
    cin >> x;
    ll even = 1, cnt = 0;
    ll curStair, req;
    while (x) {
      curStair = (even * 2) - 1;
      req = curStair * even;
      if (x - req >= 0) {
        x -= req;
        cnt++;
      } else {
        break;
      }
      even *= 2;
    }
    std::cout << cnt << std::endl;
  }
  return 0;
}
