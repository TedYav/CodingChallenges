#include <iostream>

int main(){
	std::ios::sync_with_stdio(false);
	int t, n, tmp, out;
	std::cin >> t;
	while(t--){
		out = 0;
		std::cin >> n;
		for(int i=0; i<n; ++i){
			std::cin >> tmp;
			if((n + ((n-(i+1))*i)) %2){
				out ^= tmp;
			}
		}
		std::cout << out << std::endl;
	}
	return 0;
}