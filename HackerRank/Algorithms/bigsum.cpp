#include <iostream>

using namespace std;

int main(){
	int n;
	long total = 0, x = 0;
	cin >> n;
	while(n--){
		cin >> x;
		total += x;
	}
	cout << total;
	return 0;
}