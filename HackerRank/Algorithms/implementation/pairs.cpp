#include <iostream>
using namespace std;

int main(){
	int n, k, *a, c = 0;
	cin >> n >> k;
	a = new int[n];
	for (int i = 0; i < n; ++i){
		cin >> a[i];
	}
	for (int i = 0; i < n; ++i){
		for (int j = i+1; j < n; ++j){
			if((a[i] + a[j]) % k == 0){
				c++;	// could've done this with ternary op, but I wanted to write c++ :)
			}
		}
	}
	cout << c << endl;
	return 0;
}