#include <bits/stdc++.h>

#include <iostream>

std::string phone_number;  // <= 100
int n;                     // 1 <= n <= 50000
std::vector<std::string> words;

std::map<int, std::vector<char>> keypad = {
    {1, {'i', 'j'}},      {2, {'a', 'b', 'c'}}, {3, {'d', 'e', 'f'}},
    {4, {'g', 'h'}},      {5, {'k', 'l'}},      {6, {'m', 'n'}},
    {7, {'p', 'r', 's'}}, {8, {'t', 'u', 'v'}}, {9, {'w', 'x', 'y'}},
    {0, {'o', 'q', 'z'}}
};

int answer_count = 50000;
std::vector<std::string> answer_words;

//=================================================================

bool check_substring(const std::string &word) {
  for (const auto &v : words) {
    //if (word == v) continue;
    auto found = v.find(word);
    if (found != std::string::npos) {
      return true;
    }
  }
  return false;
}

void solve(int index, std::string cur_word, std::vector<std::string> &accum) {
  // 부분 문자열 검사
  if (!check_substring(cur_word)) {
    return;
  }

  // 문자 찾았다면, 현재 문자에서 해당 문자 없애고 계속 탐색
  auto it = std::find(words.begin(), words.end(), cur_word);
  if (it != words.end()) {
    accum.emplace_back(*it);

    // 폰 번호 길이에 도달하면 종료
    if (index == phone_number.size()) {
      if (answer_count > accum.size()) {
        answer_words = accum;
      }
      accum.pop_back();
      return;
    }

    auto alphas = keypad[phone_number[index] - '0'];
    for (const auto alpha : alphas) {
      solve(index + 1, std::string(1,alpha), accum);
    }
    accum.pop_back();
  }

  auto alphas = keypad[phone_number[index]-'0'];
  for(const auto alpha : alphas) {
    solve(index+1, cur_word + alpha, accum);
  }
}

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  std::cin >> phone_number;
  std::cin >> n;
  for (int i = 0; i < n; i++) {
    std::string word;
    std::cin >> word;
    words.emplace_back(std::move(word));
  }

  std::sort(words.begin(), words.end(), [](const auto &a, const auto &b) {
    return a.size() > b.size();
  });

  std::vector<std::string> accumulated_words;
  int index = 0;
  auto start_words = keypad[phone_number[index] - '0'];
  for (const auto v : start_words) {
    solve(index+1, std::string(1, v), accumulated_words);
  }

  if (answer_words.empty()) {
    std::cout << "0\nNo solution.";
  } else {
    std::cout << answer_words.size() << "\n";
    for (const auto &v : answer_words) {
      std::cout << v << "\n";
    }
  }
}