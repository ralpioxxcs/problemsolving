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
  cin >> T;
  while (T--) {
    int n;
    string s;
    bool t = false;
    cin >> n;
    cin >> s;
    // solve
    // Breach (even)
    if (n % 2 == 0) {
      for (int i = n - 1; i >= 0; i-=2) {
        int temp = s[i] - '0';
        if (temp % 2 == 0) {
          std::cout << "2" << std::endl;
          t = true;
          break;
        }
      }
      if (!t) std::cout << "1" << std::endl;
    } else if (n % 2 == 1) {
      for (int i = n-1; i >= 0; i-=2) {
        int temp = s[i] - '0';
        if (temp % 2 != 0) {
          std::cout << "1" << std::endl;
          t = true;
          break;
        }
      }
      if (!t) std::cout << "2" << std::endl;
    }
  }
  return 0;
}

