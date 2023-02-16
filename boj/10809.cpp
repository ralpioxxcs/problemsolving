#include <bits/stdc++.h>
#include <iostream>

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  std::string word;
  std::cin >> word;

  std::map<char, int> alphabets;
  for (char w = 'a'; w <= 'z'; w++) {
    alphabets[w] = -1;
  }

  int i = 0;
  for (const auto &v : word) {
    if (alphabets[v] == -1) {
        alphabets[v] = i;
    }
    i++;
  }
  for (const auto &[k, v] : alphabets) {
    std::cout << v << " ";
  }
}