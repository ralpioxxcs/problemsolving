#include <bits/stdc++.h>
#include <iostream>

int n{0};                        // 듣도 못한 사람
int m{0};                        // 보도 못한 사람
std::map<std::string, int> mens;

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cout.tie(nullptr);
  std::cin.tie(nullptr);

  std::cin >> n >> m;

  for (int i = 0; i < n; i++) {
    std::string name;
    std::cin >> name;
    mens[name] = 1;
  }

  int count{0};
  std::vector<std::string> dbj; // 듣보잡
  for (int i = 0; i < m; i++) {
    std::string name;
    std::cin >> name;
    if(mens.find(name) != mens.end()) {
      count++;
      dbj.emplace_back(name);
    }
  }
  std::cout << count << "\n";
  std::sort(dbj.begin(), dbj.end());
  for(const auto&v:dbj) {
    std::cout << v << "\n";
  }

  return 0;
}