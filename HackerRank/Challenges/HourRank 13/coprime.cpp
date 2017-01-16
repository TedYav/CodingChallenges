#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

int gcd(int a, int b){
	if( b == 0){
		return a;
	}
	else{
		return gcd(b, a % b);
	}
}

int main(){
    int n, c = 0;
    cin >> n;
    for(int k = 6; k <= n; ++k){
    	// partial credit brute force solution
    	for(int j = 2; j <= k/2; ++j){
    		if(k % j == 0){
    			if(gcd(k/j,j) == 1){
    				c++;
    			}
    		}
    	}
    }
    cout << c/2 << endl;
    return 0;
}
