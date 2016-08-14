#include <iostream>

using namespace std;

int main(){
	int n,c,t;
	cin >> n;
	while(n--){
		cin >> c;
		t += c;
	}
	cout << t;
	return 0;
}