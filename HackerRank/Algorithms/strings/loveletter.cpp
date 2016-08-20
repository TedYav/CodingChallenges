#include <iostream>
#include <string>

int main(){
	int t, c;
	std::string s;
	std::cin >> t;
	while(t--){
		c = 0;
		std::cin >> s;
		std::string::iterator i = s.begin();
		std::string::reverse_iterator j = s.rbegin();
		while(i != s.begin() + s.length()/2){
			c += abs(*i++ - *j++);
		}
		std::cout << c << std::endl;
	}
}