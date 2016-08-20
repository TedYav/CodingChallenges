#include <iostream>
#include <string>

int main(){
	int t;
	std::string s;
	bool funny;
	std::cin >> t;
	while(t--){
		funny = true;
		std::cin >> s;
		std::string::iterator i = s.begin();
		std::string::reverse_iterator e = s.rbegin();
		while(funny && i != s.end()-1){
			funny = abs(*(i+1) - *i) == abs(*(e+1) - *e);			
			i++,e++;
		}
		std::cout << (funny ? "Funny" : "Not Funny") << std::endl;
	}
	return 0;
}