#include <iostream>
using namespace std;

int main(){
	int l, r, a = 1023, b = 0;
	cin >> l >> r;
	for(int i=l; i <= r; i++){
		a &= i;
		b |= i;
	}
	cout << (a^b) << endl;
	return 0;
}