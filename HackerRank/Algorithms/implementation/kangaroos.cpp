#include <iostream>
using namespace std;

int main(){
	int x1, v1, x2, v2;
	bool success = false;
	cin >> x1 >> v1 >> x2 >> v2;
	if(v2 < v1){
		success = (((x1 - x2)/(v2 - v1)) >= 0) && (((x1 - x2)%(v2 - v1)) == 0);
	}
	cout << (success ? "YES" : "NO") << endl;
}