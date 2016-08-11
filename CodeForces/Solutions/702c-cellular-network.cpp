/*
  Problem Statement: http://codeforces.com/problemset/problem/702/C

  Solution:
  	This is a simple binary search problem. We're trying to find the
  	minimum distance such that the towers cover all cities. We have no
  	idea what this is going to be, except that it is an integer, so we
  	set our lower bound to 0 and upperbound to INT_MAX. We then set our
  	test value to half way between the two. We adjust the upper and 
  	lower bounds on each iteration performing a binary search, until
  	they differ by 1.

  	Before returning, we check if the lower bound works as well (which
  	it will in the corner case where the answer is 0). Otherwise we
  	return the upper bound, as this is the minimum viable distance.

  	To check if a range works, we iterate through the cities and towers
  	arrays. We start both at the beginning. We check on each iteration
  	if the current selected tower covers the current selected city.

  	If it does, we increment the city index (so we're going to check
  	the next city). If it doesn't, we increment the tower index (to see
  	if the next tower will cover the city.) Eventually, we run out of 
  	towers or cities, and then we return the value of our found variable.

  	If we got to the last city, and it was found, then we know we succeeded.

  	However, if we got to the last tower, without finding a city, we know 
  	we failed. This is because we ONLY check the next city once we have
  	found a tower that covers the current city. Thus, if we run out of
  	towers, and found == false currently, it means we couldn't cover
  	all cities with the current range.
*/

#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <climits>

using namespace std;

int* populate(int numargs){
    int* target = new int[numargs];
    string line;
    getline(cin, line);;
    stringstream ss(line);
    for(int i=0; i<numargs; i++){
        ss >> target[i];
    }
    return target;
}


bool checkDistance(int range,int numCities,int numTowers,int* cities,int* towers){
	bool found = true;
	for(int i=0, j=0; (i<numCities) && (j<numTowers);){
		found = abs(cities[i] - towers[j]) <= range;
		if(found){
			i++;
		}else{
			j++;
		}
	}
	return found;
}

int main(){
	int* params = populate(2);
	int* cities = populate(params[0]);
	int* towers = populate(params[1]);

	int test, lowerBound = 0, upperBound = INT_MAX;
	while(upperBound - lowerBound > 1){
		test = lowerBound + (upperBound - lowerBound)/2;
		if(checkDistance(test, params[0], params[1], cities, towers)){
			upperBound = test;
		}else{
			lowerBound = test;
		}
	}

	cout << (checkDistance(lowerBound, params[0], params[1], cities, towers) ? lowerBound : upperBound);
	return 0;
}