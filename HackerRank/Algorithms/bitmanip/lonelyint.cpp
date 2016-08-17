#include <iostream>
using namespace std;

int main(){
	int n, t, o = 0;
	cin >> n;
	while(n--){
		cin >> t;
		o = o ^ t;
	}
	cout << o << endl;
	return 0;
}