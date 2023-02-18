#include <iostream>
#include <bits/stdc++.h>
int n; // <= 300000
int k; // <= n
std::vector<int> heights;
int answer;
void solve() {}
int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);
  std::cin >> n >> k;
  for(int i=0; i<n; i++) {
    int height;
    std::cin >> height;
    heights.emplace_back(height);
  }

  std::vector<int> heights_diff;
  for (int i = 1; i < n; i++) {
    heights_diff.emplace_back(heights[i] - heights[i - 1]);
  }
  std::sort(heights_diff.begin(), heights_diff.end());
  answer = std::accumulate(heights_diff.begin(), heights_diff.begin()+(n-k), 0);
  std::cout << answer;
}

2 2 1 4 1 5

1 1 2 2 4 5