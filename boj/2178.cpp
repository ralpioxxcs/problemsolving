#include <bits/stdc++.h>

#include <iostream>

int n, m;
int maze[101][101];
int visited[101][101];
int answer{0};
std::queue<std::pair<int, int>> q;

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void solve() {
  visited[0][0] = 1;
  q.push({0, 0});

  while (!q.empty()) {
    auto coords = q.front();
    q.pop();

    for (int i = 0; i < 4; i++) {
      int nx = coords.first + dx[i];
      int ny = coords.second + dy[i];
      if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
        continue;
      }
      if (visited[nx][ny] == 1) {
        continue;
      }
      if (maze[nx][ny] != 0) {
        maze[nx][ny] = maze[coords.first][coords.second] + 1;
        q.push({nx, ny});
        visited[nx][ny] = 1;
      }
    }
  }
  answer = maze[n-1][m-1];
}

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);
  std::cin >> n >> m;
  for (int i = 0; i < n; i++) {
    std::string row;
    std::cin >> row;
    for (int j = 0; j < m; j++) {
      maze[i][j] = row[j] - '0';
      visited[i][j] = 0;
    }
  }
  solve();
  std::cout << answer;
}