#include <iostream>

using namespace std;

int main(){
	int n, t, *arr, lsum = 0, rsum = 0;
	bool found = false;
	cin >> t;
	while(t--){
		cin >> n;
		arr = new int[n];
		rsum = 0;
		lsum = 0;
		found = true;
		cin >> arr[0];
		for (int i = 1; i < n; ++i){
			found = false;
			cin >> arr[i];
			rsum += arr[i];
		}
		for(int i=1; i<n; i++){
			lsum += arr[i-1];
			rsum -= arr[i];
			if(lsum == rsum){
				found = true;
				break;
			}
		}
		cout << (found ? "YES" : "NO") << endl;
	}
	return 0;
}