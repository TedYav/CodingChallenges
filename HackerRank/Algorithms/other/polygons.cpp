#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, result = 0, partialSum = 0;
    cin >> n;
    vector<int> data(n);
    for(int i = 0; i<n; i++){
    	cin >> data[i];
    }
    sort(data.begin(), data.end());

    if(data.size()<3){
    	result = 3 - data.size();
    }else{
    	for (int i = 0; i < n-1; partialSum += data[i], i++)
    	{
    		;
    	}
    	if(partialSum <= data[n-1]){
    		result = 1;
    	}
    }
    cout << result;
    return 0;
}
