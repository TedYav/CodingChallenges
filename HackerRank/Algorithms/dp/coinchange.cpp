// recurrence:
// W(n,m) = number of ways to make n with first m coins
// W(n,m) = W(n,m-1) + W(n-C[m], m) where C[m] = value of coin m
// thank you to a hacker rank poster for pointing this out as I was double counting
// I was doing: W(n,m) = W(n-C[m], m) + W(C[m],m) == double counting lots of cases

#include <iostream>

int main(){
	// initialization
	int64_t ** dp;
	int m,n,*c;
	std::cin >> n >> m;
	// do n+1 so we can calculate making 0 change
	dp = new int64_t*[n+1];
	// makes it easier to select coin j
	c = new int[m+1];
	c[0] = 0;
	dp[0] = new int64_t[m+1];
	dp[0][0] = 1;
	for(int i=1; i<=m; i++){
		std::cin >> c[i];
		dp[0][i] = 1;
	}
	// initializing: can make 0 cents with any number of coins in only 1 way
	for(int i=1; i<n+1; i++){
		// m + 1 so we can calculate using 0 coins
		dp[i] = new int64_t[m+1];
		dp[i][0] = 0;
	}

	// dynamic programming :)
	for(int i=1; i<=n; i++){
		for(int j=1; j<=m; j++){
			dp[i][j] = dp[i][j-1] + (i - c[j] >= 0 ? dp[i-c[j]][j] : 0);
		}
	}

	std::cout << dp[n][m] << std::endl;

	return 0;
}