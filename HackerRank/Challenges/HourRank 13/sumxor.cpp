#include <iostream>
using namespace std;

int main(){
	long n, c = 1;	// 0 always works for XOR
	cin >> n;
	while(n > 0){
		if(!(n & 1)){
			c *= 2;
		}
		n >>= 1;
	}
	cout << c << endl;
	return 0;
}