#include <iostream>
#include <queue>
#include <string>
#include <vector>
using namespace std;

string solution(vector<string> cards1, vector<string> cards2, vector<string> goal) {
  std::queue<std::string> cards1_queue, cards2_queue, goal_queue;
  for (const auto& v : cards1) {
    cards1_queue.push(v);
  }
  for (const auto& v : cards2) {
    cards2_queue.push(v);
  }
  for (const auto& v : goal) {
    goal_queue.push(v);
  }

  // 목표 단어들이 없어질때 까지
  while (!goal_queue.empty()) {
    auto word = goal_queue.front();
    // 카드뭉치1의 맨 앞 단어와 같다면
    if (word == cards1_queue.front()) {
      if (!cards1_queue.empty()) {
        cards1_queue.pop();
      }
      // 카드뭉치2의 맨 앞 단어와 같다면
    } else if (word == cards2_queue.front()) {
      if (!cards2_queue.empty()) {
        cards2_queue.pop();
      }
    } else {
      break;
    }
  
    goal_queue.pop();
  }

  std::string answer;

  // 모두 소진 했다면 성공
  if (goal_queue.empty()) {
    answer = "Yes";
  } else {
    answer = "No";
  }

  return answer;
}