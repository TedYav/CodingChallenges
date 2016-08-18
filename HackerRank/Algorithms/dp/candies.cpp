#include <iostream>

using namespace std;

int main(){
	int n, *r, *c, t=0, min = 0;
	bool again = true;
	cin >> n;
	r = new int[n+2];
	c = new int[n+2];
	r[0] = r[n+1] = -1;
	c[0] = c[n+1] = 0;
	for(int i=1; i<=n; i++){
		cin >> r[i];
		c[i] = 1;
	}
	
	// get diffs
	for(int i=1; i<=n; i++){
		if(r[i] > r[i-1] && c[i] <= c[i-1]){
			c[i] = c[i-1] + 1;
		}else if(r[i] < r[i-1] && c[i] >= c[i-1]){
			c[i] = c[i-1] - 1;
		}
		min = (c[i] < min ? c[i] : min);
	}

	for(int i=1; i<=n; i++){
		c[i] += (min * -1) + 1;
		if(r[i] <= r[i-1] && r[i] <= r[i+1]){
			c[i] = 1;
		}
		t += c[i];
		cout << c[i] << endl;
	}

	for(int i=1; i<= n; i++){
		if((r[i] > r[i-1] && c[i] <= c[i-1]) || (r[i] > r[i+1] && c[i] <= c[i+1])){
			cout << "FAIL" << endl;
		}
	}
	cout << t << endl;
	return 0;
}