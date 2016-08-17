#include <iostream>
using namespace std;

int main(){
	int t, n, k, tmp, p;
	cin >> t;
	while(t--){
		cin >> n >> k;
		p = 0;
		for(int i=0; i<n; ++i){
			cin >> tmp;
			p += (tmp <= 0 ? 1 : 0);
		}
		cout << ((p < k) ? "YES" : "NO") << endl;
	}
}