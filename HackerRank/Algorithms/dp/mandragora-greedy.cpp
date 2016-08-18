#include <iostream>
#include <vector>
#include <algorithm>
#include <array>

using namespace std;

// greedy algo worked--dp algo was too slow!!

int main(){
	int t, n;
	long mExp;
	int *h;

	cin >> t;
	while(t--){
		cin >> n;
		h = new int[n+1];
		h[0] = 0;
		for (int i = 1; i <= n; ++i)
		{
			cin >> h[i];
		}
		sort(h, h+n+1);
		mExp = -1;
		long sub = 0, tmp=0;
		for(int i=n; i>=0; --i){
			sub += h[i];
			tmp = sub * i;
			if(tmp > mExp){
				mExp = tmp;
			}else{
				break;
			}
		}
		cout << mExp << endl;
	}
	return 0;
}