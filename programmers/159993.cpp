#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

constexpr char START{'S'};
constexpr char EXIT{'E'};
constexpr char LEVER{'L'};
constexpr char PATH{'O'};
constexpr char WALL{'X'};

char map[101][101];
int moves[101][101];
bool visited[101][101];

std::pair<int, int> start_coords;
std::pair<int, int> exit_coords;
std::pair<int, int> lever_coords;

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int solution(vector<string> maps) {
  int answer = 0;

  // 입력
  int col_count = 0;
  int row_count = 0;
  for (const auto &v : maps) {
    auto row = v;
    row_count = 0;
    for (const auto &r : row) {
      if (r == START) {
        start_coords = {col_count, row_count};
      } else if (r == EXIT) {
        exit_coords = {col_count, row_count};
      } else if (r == LEVER) {
        lever_coords = {col_count, row_count};
      }
      map[col_count][row_count]= r;
      moves[col_count][row_count]= 0;
      visited[col_count][row_count]= false;
      row_count++;
    }
    col_count++;
  }

  std::queue<std::pair<int, int>> q;
  bool lever_exists{false};
  bool exit_succeed{false};
    
  q.push({start_coords.first, start_coords.second});
  visited[start_coords.first][start_coords.second] = true;

  while (!q.empty()) {
    auto cur_coords = q.front();
    q.pop();

    int cx = cur_coords.first;
    int cy = cur_coords.second;

    // 탈출구
    if (map[cx][cy] == EXIT) {
      if (lever_exists) {
        answer = moves[cx][cy];
        exit_succeed = true;
        break;
      }
    // 레버
    } else if (map[cx][cy] == LEVER) {
      // 방문 배열 초기화
      for (int i = 0; i < col_count; i++) {
        for (int j = 0; j < row_count; j++) {
          visited[i][j] = false;
        }
      }        
      // 큐 초기화
      q = {};
      visited[cx][cy] = true;
      lever_exists = true;
    }

    for (int i = 0; i < 4; i++) {
      auto nx = cx + dx[i];
      auto ny = cy + dy[i];

      if (nx < 0 || ny < 0 || nx >= col_count || ny >= row_count) {
        continue;
      }
      if (map[nx][ny] == WALL) {
        continue;
      }
      if (visited[nx][ny]) {
        continue;
      }
      visited[nx][ny] = true;
      q.push({nx, ny});
      moves[nx][ny] = moves[cx][cy] + 1;
    }
  }

  if (exit_succeed) {
    return answer;
  } else {
    return -1;
  }
}