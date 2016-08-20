#include <iostream>

inline unsigned int shiftzero(unsigned int a){
	unsigned int shifts = 0;
	 while(a>0){
	 	a >>= 1;
	 	shifts++;
	 }
	 return shifts;
}

int main(){
	unsigned int t, a, b, res;
	std::cin >> t;
	while(t--){
		std::cin >> a >> b;
		res = (a & b) >> shiftzero(b-a) << shiftzero(b-a);
		std::cout << res << std::endl;
	}
	return 0;
}