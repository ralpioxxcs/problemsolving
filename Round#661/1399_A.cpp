#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#define TEST

int main() {
	std::cin.tie(0)->sync_with_stdio(0);
	std::cout.tie(0);
#ifdef TEST
	freopen("input.txt", "r", stdin);
#endif
	int T;
    std::string ans;
    int n; // (1<=n<=50)
	std::cin >> T;
	 while (T--) {
         std::cin >> n;
         std::vector<int> a(n);
         for(int i=0; i<n;i++) {
             std::cin >> a[i];
         }
         sort(a.begin(),a.end());
         int min_val = 101;
         for(int i=0; i<n-1; i++) {
             if(abs(a[i]-a[i+1]) <=1) {
                 continue;
             } else {
                 std::cout<<"NO\n";
                 break;
             }
         }
		std::cout <<"YES\n";
	}
	return 0;
}