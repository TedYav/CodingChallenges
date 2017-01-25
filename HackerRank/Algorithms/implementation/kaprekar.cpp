#include <iostream>

// terrible implementation!
long pow(long base, long exponent){
	if(exponent <= 0){
		return 1;
	}else if(exponent == 1){
		return base;
	}else{
		return base * pow(base, exponent - 1);
	}
}

bool is_kaprekar_number(long number){
	long orig_number = number;
	number *= number;
	long num_digits = 1;
	while(number / pow(10,num_digits) > 0){
		num_digits++;
	}
	long left = num_digits / 2;
	long right = (num_digits / 2) + (num_digits % 2);

	long left_sum = 0;
	long right_sum = 0;

	long current_mod = pow(10, num_digits);
	long current_pow = pow(10, num_digits - 1);

	long current_place_pow = pow(10, left - 1);
	for(long i = 0; i<left; ++i){
		left_sum += current_place_pow * ((number % current_mod)/current_pow);
		current_place_pow /= 10;
		current_mod /= 10;
		current_pow /= 10;
	}
	current_place_pow = pow(10, right - 1);
	for(long i=0; i<right; ++i){
		right_sum += current_place_pow * ((number % current_mod)/current_pow);
		current_place_pow /= 10;
		current_mod /= 10;
		current_pow /= 10;
	}
	return (left_sum + right_sum == orig_number);
}

int main(){
	long p, q;
	std::cin >> p >> q;
	bool nums_found = false;
	for(long i=p; i<=q; ++i){
		if(is_kaprekar_number(i)){
			std::cout << i << " ";
			nums_found = true;
		}
	}
	if(!nums_found){
		std::cout << "INVALID RANGE";
	}
	std::cout << std::endl;
}