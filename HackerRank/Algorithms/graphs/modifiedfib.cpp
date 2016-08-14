#include <iostream>
#include <cstdint>

struct uint256_t {
	std::uint64_t bits[4];
};

int main(){
	uint256_t x;
	std::cin >> x;
	std::cout << x;
	return 0;
}