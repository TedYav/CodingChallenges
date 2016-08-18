#include <iostream>
int main(){
	unsigned int t,n;
	std::cin >> t;
	while(t--){
		std::cin >> n;
		std::cout << ~n << std::endl;
	}
}