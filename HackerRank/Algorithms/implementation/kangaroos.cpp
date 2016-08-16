#include <iostream>
using namespace std;

int gcd(int a, int b){
	if(b > a){
		a ^= b;
		b ^= a;
		a ^= b;
	}
	return (b == 0 ? a : gcd(b, a%b));
}

int hops(int x,int v,int dist){
	cout << "CHECKING HOPS: X: " << x << " V: "<< v << " DIST" << dist << endl;
	cout << "HOPS: " << (dist-x)/v << endl;
	return (dist-x)/v;
}

int main(){
	int x1, v1, x2, v2, lcm, h1=1, h2=0, r, gd;
	bool success = false;
	cin >> x1 >> v1 >> x2 >> v2;
	if(v2 < v1){
		int tmp = x1 > x2 ? x2 : x1;
		x1 -= tmp;
		x2 -= tmp;
		gd = gcd(v1, v2);
		lcm = (v1*v2) / gd;
		cout << "X1 v1 and v2: " << (x1 % v1) % gd << endl;
		cout << "X2 v2 and v1: " << (x2 % v2) % gd << endl;
		cout << "GCD: " << gd << endl;
		if((x1 % v1) % gd == (x2 % v2) % gd){
			cout << "SAME" << endl;
			r = (x1 % v1) % gd;
			for(int i=1; h1 > h2; ++i){
				h1 = hops(x1,v1,lcm*i + r);
				h2 = hops(x2,v2,lcm*i + r);
				if(h1==h2){
					success = true;
					break;
				}
			}
		}
	}

	cout << (success ? "YES" : "NO") << endl;
}