#include <iostream>

int main(){
	std::ios::sync_with_stdio(false);
	int n, a[1001], t;
	for(int i=0; i<1001; ++i){
		a[i] = 0;
	}
	std::cin >> n;
	for(int i=0; i<n; ++i){
		std::cin >> t;
		a[t]++;
	}
	std::cout << n << std::endl;
	for(int i=0, c=n; i<1001 && c > 0; ++i){
		if(a[i]){
			c -= a[i];
			if(c){
				std::cout << c << std::endl;
			}
		}
	}
	return 0;
}