#include <iostream>
using namespace std;

// returns an upper bound for position in array
// guess will always equal lower bound when
// loop terminates
int bsearch(int k, int arr[], int len){
	int lo = 0, hi = len, guess = (lo+hi)/2;
	while(hi - lo > 1){
		if(arr[guess] > k){
			hi = guess;
		}else if(arr[guess] < k){
			lo = guess;
		}else{
			lo = guess;
			hi = guess + 1;
		}
		guess = (lo + hi) / 2;
	}
	return arr[guess] == k ? guess : hi;
}

int main(){
	int k, n;
	int *arr;
	cin >> k >> n;
	arr = new int[n];
	for (int i = 0; i < n; ++i){
		cin >> arr[i];
	}
	cout << bsearch(k, arr, n);
}

