#include <bits/stdc++.h>
#define TEST
using namespace std;
int main() {
  cin.tie(0)->sync_with_stdio(0);
  cout.tie(0);
#ifdef TEST
  freopen("input.txt", "r", stdin);
#endif
  int d, sumTime;
  cin >> d >> sumTime;
  std::vector<int> minarr(d);
  std::vector<int> maxarr(d);
  int minSum = 0, maxSum = 0;
  for (int i = 0; i < d; ++i) {
    cin >> minarr[i];
    cin >> maxarr[i];
    minSum += minarr[i];
    maxSum += maxarr[i];
  }
  // solve
  if (maxSum < sumTime || minSum > sumTime) {
    std::cout << "NO" << std::endl;
  } else {
    std::cout << "YES" << std::endl;
    for (int i = 0; i < d; ++i) {
      int v = min(minarr[i] + sumTime - minSum, maxarr[i]);
      std::cout << v <<" ";
      minSum -= minarr[i];
      maxSum -= maxarr[i];
      sumTime -= (v);
    }
  }
  return 0;
}
