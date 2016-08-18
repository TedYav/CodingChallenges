#include <iostream>
#include <vector>
#include <algorithm>
#include <array>

using namespace std;

// strategy --> largest noncontiguous subsequence of size n, n-1, n-2 etc
// multiply

int main(){
	int t, n;
	long mExp;
	long *h;
	long ** dp;

	cin >> t;
	while(t--){
		cin >> n;
		h = new long[n];
		dp = new long*[n];
		cin >> h[0];
		dp[0] = new long[n];
		dp[0][0] = h[0];
		for (int i = 1; i < n; ++i)
		{
			cin >> h[i];
			dp[i] = new long[n];
			dp[0][i] = dp[0][i-1] + h[i];
		}
		for(int e=1; e < n; e++){
			for(int k=e; k < n; k++){
				dp[e][k] = max(dp[e][k-1] + h[k], dp[e-1][k-1]);
				// cout << dp[e][k] << endl;
			}
		}
		long prev = -1;
		for(long i=0; i<n; i++){
			mExp = dp[i][n-1]*(i+1);
			if(prev > mExp){
				mExp = prev;
				break;
			}
			prev = dp[i][n-1]*(i+1);
		}	
		cout << mExp << endl;
	}
	return 0;
}