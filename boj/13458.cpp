#include <bits/stdc++.h>
#include <iostream>

long long n;
long long persons[1000001];
long long b,c;
long long answer;

void solve() {
  for(int i=0; i<n; i++) {
    auto a = persons[i];
    if (b > a) {
      answer++;
      continue;
    }
    auto rem = a - b;
    answer++;
    auto boo = int(rem/c);
    answer += boo;
    if (rem % c > 0) {
      answer += 1;
    }
  }
}

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);
  std::cin >> n;
  for(int i=0; i<n; i++) {
    std::cin >> persons[i];
  }
  std::cin >> b >> c;
  solve();
  std::cout << answer;
}