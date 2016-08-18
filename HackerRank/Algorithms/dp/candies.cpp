#include <iostream>

using namespace std;

int main(){
	int n, *r, *c;
	long t = 0;
	bool again = true;
	cin >> n;
	r = new int[n+2];
	c = new int[n+2];
	r[0] = r[n+1] = 100000000;
	c[0] = c[n+1] = -1;
	for(int i=1; i<=n; i++){
		cin >> r[i];
		c[i] = 1;
	}
	
	while(again){
		again = false;
		for(int i=1; i<=n; i++){
			if(r[i] > r[i-1] && c[i] <= c[i-1]){
				again = true;
				c[i] = c[i-1] + 1;
			}else if(r[i] > r[i+1] && c[i] <= c[i+1]){
				again = true;
				c[i] = c[i+1] + 1;
			}

			if(r[n+1-i] > r[n-i] && c[n+1-i] <= c[n-i]){
				again = true;
				c[n+1-i] = c[n-i] + 1;
			}else if(r[n+1-i] > r[n+2-i] && c[n+1-i] <= c[n+2-i]){
				again = true;
				c[n+1-i] = c[n+2-i] + 1;
			}
		}
	}

	for(int i=1; i<=n; i++){
		t += c[i];
	}
	
	cout << t << endl;
	return 0;
}