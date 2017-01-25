#include <iostream>
#include <vector>

int main(){
	int n, k, temp, energy = 100;
	std::vector<int> clouds;
	std::cin >> n >> k;
	for(int i=0; i<n; ++i){
		std::cin >> temp;
		clouds.push_back(temp);
	}

	int i = 0;
	do{
		energy -= 1;
		i += k;
		if(clouds[i%n] == 1){
			energy -= 2;
		}
	}while(i%n != 0);
	std::cout << energy << std::endl;
}