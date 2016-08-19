#include <iostream>

int main(){
	std::ios::sync_with_stdio(false);

	int n, a[1000005], dp[1000005], t, ms;

	std::cin >> n;

	for (int i = 0; i < n; ++i){
		std::cin >> a[i];
		dp[i] = 1;
	}

	for(int i=1; i<n; ++i){
		ms = 0;
		for(int j=i-1; j>=0; --j){
			if(a[j] < a[i]){
				if(dp[j] > ms){
					ms = dp[j];
				}
			}
		}
		dp[i] = ms + 1;
		if(dp[i] > t){
			t = dp[i];
		}
	}

	std::cout << t << '\n';
	return 0;
}