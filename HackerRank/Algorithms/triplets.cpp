#include <iostream>

using namespace std;

int main(){
	int s[6],a=0,b=0;
	for (int i = 0; i < 6; ++i)
	{
		cin >> s[i];
	}
	for(int i=0; i<3; i++){
		a += s[i] > s[i+3] ? 1 : 0;
		b += s[i] < s[i+3] ? 1 : 0;
	}
	cout << a << " " << b;
	return 0;
}