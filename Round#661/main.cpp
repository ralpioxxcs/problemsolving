#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

#define TEST

int main() {
  std::cin.tie(0)->sync_with_stdio(0);
  std::cout.tie(0);
#ifdef TEST
  freopen("input.txt", "r", stdin);
#endif
  int T;
  int n;
  int ans = 0;
  std::cin >> T;
  while (T--) {
    std::cin >> n;
    std::vector<int> w(n);
    for(int i=0; i<n; i++) {
      std::cin >> w[i];
    }
    std::cout<<ans<<std::endl;
  }
  return 0;
}
