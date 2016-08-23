#include <iostream>
#include <vector>

int main(){
	std::ios::sync_with_stdio(false);
	int t,n;
	std::vector<unsigned long long> dp;

	std::cin >> t;

	while(t--){
		std::cin >> n;
		dp = std::vector<unsigned long long>(n+1);
		// 2 * n-1 - 1 because all vert doesn't count
		// 2 * n-4 - 1 if n%4 == 0 else - 0
		dp[0] = dp[1] = dp[2] = dp[3] = 1;
		dp[4] = 2;
		for(int i=5; i<=n; ++i){
			// dp[i] = (2*(dp[i-1] - 1)) + (2 * (dp[i-4] - (i%4 == 0 ? 1 : 0)));
			// if it's divisible by 4, there's one extra way -- offsets the all vertical
			dp[i] = (2*dp[i-1] - (i%4 == 0 ? 0 : 1));	
		}
		std::cout << dp[n] << std::endl;
	}
}