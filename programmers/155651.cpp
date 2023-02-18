#include <string>
#include <vector>
#include <iostream>
#include <string>
#include <bits/stdc++.h>

using namespace std;

// t1이 t2보다 더 이른 시간일 경우 -> false
// t1이 t2보다 더 늦은 시거나 같은 시간일 경우 -> true
bool time_diff(std::string &t1, std::string &t2) {
    auto t1_hour = std::atoi(t1.substr(0,2).c_str());
    auto t1_minutes = std::atoi(t1.substr(3,5).c_str());
    auto t2_hour = std::atoi(t2.substr(0,2).c_str());
    auto t2_minutes = std::atoi(t2.substr(3,5).c_str());
    if(t1_hour == t2_hour) {
        if (t1_minutes >= t2_minutes) {
            return true;
        } else {
            return false;
        }
    } else {
        if (t1_hour >= t2_hour) {
            return true;
        } else {
            return false;
        }
    }
}

std::string time_add(std::string &t, int add_minutes) {
    auto h = std::atoi(t.substr(0,2).c_str());
    auto m = std::atoi(t.substr(3,5).c_str());
    h += int((m+add_minutes)/60);
    m = ((m+add_minutes)%60);
    std::string hstr{std::to_string(h)}, mstr{std::to_string(m)};
    if(h<10) {
        hstr = "0" + std::to_string(h);
    }
    if(m<10) {
        mstr = "0" + std::to_string(m);
    }
    return hstr + ":" + mstr;
}

bool sort_by_begin(const std::vector<std::string> t1, const std::vector<std::string> t2) {
    auto hour_t1 = std::atoi(t1[0].substr(0,2).c_str());
    auto minutes_t1 = std::atoi(t1[0].substr(3,5).c_str());
    auto hour_t2 = std::atoi(t2[0].substr(0,2).c_str());
    auto minutes_t2 = std::atoi(t2[0].substr(3,5).c_str());
    if(hour_t1 == hour_t2) {
        return minutes_t1 < minutes_t2;
    } else {
        return hour_t1 < hour_t2;
	}
}

bool sort_by_end(const std::vector<std::string> t1, const std::vector<std::string> t2) {
    auto hour_t1 = std::atoi(t1[1].substr(0,2).c_str());
    auto minutes_t1 = std::atoi(t1[1].substr(3,5).c_str());
    auto hour_t2 = std::atoi(t2[1].substr(0,2).c_str());
    auto minutes_t2 = std::atoi(t2[1].substr(3,5).c_str());
    if(hour_t1 == hour_t2) {
        return minutes_t1 < minutes_t2;
    } else {
        return hour_t1 < hour_t2;
	}
}

int solution(vector<vector<string>> book_time) {
    int answer = 0; // 방의 갯수
    
    // 시작 시간 기준으로 오름차순 정렬
    std::sort(book_time.begin(), book_time.end(), sort_by_begin);
    
    std::vector<std::vector<std::string>> occupied_rooms;
    auto cur_begin_time = book_time[0][0];
    auto cur_end_time = book_time[0][1];
    
    // 첫 번째 입실 방 삽입하여 초기화
    ++answer;
    occupied_rooms.emplace_back(book_time[0]);
    
    // 두 번째 입실 방 부터 체크
    for(int i=1; i<book_time.size(); i++) {
        auto begin_cur = book_time[i][0];
        auto end_cur = book_time[i][1];
        
        // 퇴실시간 빠른 순으로 정렬
        std::sort(occupied_rooms.begin(), occupied_rooms.end(), sort_by_end);
  
        bool reuse{false};
        int room_index{0};
        for(int j=0; j < occupied_rooms.size(); j++) {
            auto end_occ = occupied_rooms[j][1];
            end_occ = time_add(end_occ, 10);
            // 현재 입실된 방들 중에 입실 가능한 곳이 있다면 저장
            if(time_diff(begin_cur, end_occ)) {
                room_index = j;
                reuse = true;
                break;
            }
        }
        // 입실 가능 -> 입실된 방 리스트에서 제거
        if(reuse) {
            occupied_rooms.erase(occupied_rooms.begin() + room_index);
        } else {
        // 입실 불가능 -> 다른 방 갯수 추가
        	++answer;
        }
        occupied_rooms.emplace_back(book_time[i]);
	}
    return answer;
}