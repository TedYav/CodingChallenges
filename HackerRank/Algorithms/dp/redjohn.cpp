#include <iostream>

inline int ceil(int num, int div){
	return (num % 2 ? (num/2) + 1 : num/2);
}

int primes(int num){
	int size = ceil(num, 2);
	int * nums = new int[size];
	int numprimes = (num >= 2 ? 1 : 0);	// 2
	if(num <= 2){
		return numprimes;
	}
	int max = size + 1;

	for(int i=0; i<size; ++i){
		nums[i] = i*2 + 1;
	}
	nums[0] = 0; // 1 isn't prime

	// approximate sqrt
	// can speed up with binary search if needed
	for(int j = max; j*j >= num; --j, max++){
		max = j;
	}

	// sieve
	for(int i=0; i<size; ++i){
		// std::cout << nums[i] << std::endl;
		if(nums[i] != 0){
			for(int j = 3*nums[i]; j <= num; j += nums[i] * 2){
				nums[j/2] = 0;
			}
		}
	}

	// total
	for(int i=0; i<size; ++i){
		numprimes += (nums[i] != 0 ? 1 : 0);
	}

	return numprimes;
}

int main(){
	std::ios::sync_with_stdio(false);
	int t, n;
	// number of arrangements possible in grid size N and I horizontal bricks
	// b(n,i)
	// answer to problem = sum b(n,i) for i from 0 to n/4	
	// b(n,i) = c(n-4i + i, n-4i)

	// in order to solve using dynamic programming
	// I'll fill out combinatoric array c[40][40] to represent all combinations,
	// then sum up to give answer
	int c[41][41];

	int combos;

	std::cin >> t;

	// build combinatoric array
	for(int i=0; i<=40; ++i){
		c[0][i] = 0;
		c[1][i] = 0;
	}

	c[1][0] = c[1][1] = 1;

	for(int i=2; i<=40; ++i){
		c[i][0] = 1;
		for(int j=1; j<=40; ++j){
			c[i][j] = (j <= i ? c[i-1][j-1] + c[i-1][j] : 0 );
		}
	}

	// run test cases
	while(t--){
		std::cin >> n;
		combos = 0;
		for(int i=0; i <= n/4; ++i){
			combos += c[n - (4*i) + i][n - (4*i)];
		}
		// std::cout << combos << std::endl;
		std::cout << primes(combos) << std::endl;
	}

	return 0;

}