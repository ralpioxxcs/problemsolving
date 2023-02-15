#include <bits/stdc++.h>
#include <iostream>

std::vector<long> ans;
long n = 0;

void append(long number) {
  ans.emplace_back(number);
  std::string numStr = std::to_string(number);
  auto last = numStr.back();
  for (long i = 0; i < long(last - '0'); i++) {
    append(std::stol(numStr + std::to_string(i)));
  }
}

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin >> n;
  if (n>1022) {
    std::cout << -1;
    return 0;
  }
  for (long i = 0; i < 10; i++) {
    append(long(i));
  }
  sort(ans.begin(), ans.end());
  std::cout << ans[n];
}