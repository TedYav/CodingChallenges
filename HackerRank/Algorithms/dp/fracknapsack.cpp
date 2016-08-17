#include <iostream>
#include <vector>

int main(){
	int t, k, n;
	std::vector<int> A;
	std::cin >> t;

	while(t--){
		std::cin >> n >> k;
		A = std::vector<int>(n);
		for (std::vector<int>::iterator i = A.begin(); i != A.end(); ++i){
			std::cin >> *i;
		}
		for (int i = 0; i < k; ++i){
			
		}
	}
	return 0;
}