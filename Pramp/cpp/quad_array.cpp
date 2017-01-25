#include <iostream>
#include <map>
#include <vector>
#include <utility>

std::vector<int> get_unique_pairs(std::map<int,std::vector<std::pair<int,int> > > lookup_table, int sum1, int sum2){
	std::vector<std::pair<int,int> > pairs1 = lookup_table.find(sum1)->second;
	std::vector<std::pair<int,int> > pairs2 = lookup_table.find(sum2)->second;
	std::vector<int> result;
	for(auto i=pairs1.begin(); i != pairs1.end(); ++i){
		for(auto j=pairs2.begin(); j != pairs2.end(); ++j){
			std::pair<int,int> pair1 = *i;
			std::pair<int,int> pair2 = *j;
			if((pair1.first != pair2.first) && (pair1.first != pair2.second) &&  (pair1.second != pair2.first) && (pair1.second != pair2.second)){
				result.push_back(pair1.first);
				result.push_back(pair1.second);
				result.push_back(pair2.first);
				result.push_back(pair2.second);
				return result;
			}
		}
	}
	return result;
}

int main(){
	int n, target, temp, temp_sum;
	std::pair <int,int> temp_tuple;
	std::vector<int> values;
	std::map<int,std::vector<std::pair<int,int> > > lookup_table;
	std::cin >> n >> target;
	
	// read values
	for(int i=0; i<n; ++i){
		std::cin >> temp;
		values.push_back(temp);
	}

	// insert pairs into map
	for(int i=0; i<n; ++i){
		for(int j=i+1; j<n; ++j){
			temp_tuple = std::make_pair(i,j);
			temp_sum = values[i] + values[j];
			auto current = lookup_table.find(temp_sum);
			if(current != lookup_table.end()){
				current->second.push_back(temp_tuple);
				lookup_table[temp_sum] = current->second;
			}else{
				std::vector<std::pair<int,int> > new_vector;
				new_vector.push_back(temp_tuple);
				lookup_table[temp_sum] = new_vector;
			}
		}
	}

	for(auto iterator = lookup_table.begin(); iterator != lookup_table.end(); iterator++){
		if(lookup_table.find(target-iterator->first) != lookup_table.end()){
			std::vector<int> result = get_unique_pairs(lookup_table, iterator->first, target - iterator->first);
			if(!result.empty()){
				std::string sep = ", ";
				std::cout << result[0] << sep << result[1] << sep << result[2] << sep << result[3] << std::endl;
				std::cout << values[result[0]] << sep << values[result[1]] << sep << values[result[2]] << sep << values[result[3]] << std::endl;
				std::cout << values[result[0]] + values[result[1]] + values[result[2]] + values[result[3]] << std::endl;
				return 0;
			}
		}
	}

	std::cout << "No result found.";
	return 1;
}