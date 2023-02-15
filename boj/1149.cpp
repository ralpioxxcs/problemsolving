#include <bits/stdc++.h>
#include <iostream>

int n{0}; // 2 <= n <= 1000
std::vector<std::vector<int>> house;

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  std::cin >> n;
  int a,b,c;
  for(int i=0; i<n; i++) {
    std::cin >> a >> b >> c;
    house.emplace_back(std::vector<int>{a,b,c});
  }
  //--------------------------------------------------
  for(int i=1; i<n; i++) {
    house[i][0] =std::min(house[i][0] + house[i-1][1], house[i][0] + house[i-1][2]); // Green or Blue
    house[i][1] =std::min(house[i][1] + house[i-1][0], house[i][1] + house[i-1][2]); // Red or Blue
    house[i][2] =std::min(house[i][2] + house[i-1][0], house[i][2] + house[i-1][1]); // Red or Green
  }
  //--------------------------------------------------
  std::vector<int> costs{house[n-1][0], house[n-1][1], house[n-1][2]};
  auto answer = *std::min_element(costs.begin(), costs.end());
  std::cout << answer << "\n";
  return 0;
}

