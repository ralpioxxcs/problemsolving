#include <bits/stdc++.h>

#include <iostream>
#include <map>

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  std::string word;
  std::cin >> word;

  std::map<char, int> alphas;
  for (char i = 'A'; i < 'Z'; i++) {
    alphas[i] = 0;
  }
  for (const auto& v : word) {
    alphas[std::toupper(v)] += 1;
  }

  char answer;
  int max = 0;
  for (const auto& [k,v] : alphas) {
    if (v > max) {
      answer = k;
      max = v;
    }
  }
  // coutn same
  for (const auto& [k,v] : alphas) {
    if (max == v && answer != k) {
      answer = '?';
    }
  }

  std::cout << answer;
}