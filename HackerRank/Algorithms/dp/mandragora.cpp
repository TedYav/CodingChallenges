#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	long t, n;
	long mExp;
	vector<long> h;
	vector<long> dp;

	cin >> t;
	while(t--){
		cin >> n;
		// 1 indexed for ease
		h = vector<long>(n+1);
		h[0] = 0;
		dp = vector<long>(n+1);
		fill(dp.begin(), dp.end(), 0);
		for(vector<long>::iterator i = (h.begin() + 1), e = h.end(); i!= e; ++i){
			cin >> *i;
		}
		sort(h.begin(), h.end());
		mExp = 0;
		for(long i=n-1; i>=0; --i){
			long tmp = 0;
			for(long j=i+1; j<=n; ++j){
				tmp += (i+1) * h[j]; 
			}
			dp[i] = tmp;
			mExp = (tmp > mExp ? tmp : mExp);
		}
		cout << mExp << endl;
	}
	return 0;
}