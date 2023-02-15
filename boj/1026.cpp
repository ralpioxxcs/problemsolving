#include <bits/stdc++.h>
#include <iostream>

int n;
std::vector<int> a,b;

int main() {
  std::ios_base::sync_with_stdio(false);

  std::cin >> n;
  int num;
  for(int i=0; i<n; i++) {
    std::cin >> num;
    a.emplace_back(num);
  }
  for(int i=0; i<n; i++) {
    std::cin >> num;
    b.emplace_back(num);
  }
  std::sort(a.begin(), a.end());
  std::sort(b.begin(), b.end(), std::greater<int>());

  int sum = 0;
  for(int i=0; i<n; i++) {
    sum += (a[i] * b[i]);
  }
  std::cout << sum << "\n";
  return 0;
}