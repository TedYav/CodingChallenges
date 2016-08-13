#include <iostream>
#include <random>
// #include <time>
using namespace std;

/* INLINE EVERYTHING
*/

void swap(int arr[], int a, int b){
	int temp = arr[b];
	arr[b] = arr[a];
	arr[a] = temp;
}

int pickPivot(int length){
	return rand() % length;
}

void sort(int arr[], int length){
	if(length > 1){
		int pivot = pickPivot(length);
		swap(arr, pivot, length-1);
		int offset = 0;
		for(int i=0; i<length - 1; i++){
			if(arr[i]<arr[length-1]){
				swap(arr,offset++,i);
			}
		}
		swap(arr, offset++,length-1);
		sort(arr, offset - 1);
		sort(arr+offset, length-offset);
	}
}

int bsearch(int arr[], int target, int length){
	int lo = 0, hi = length, test;
	if(target >= arr[length - 1] || target < arr[0]){
		return target >= arr[length - 1] ? length : 0;
	}
	while(hi - lo > 1){
		test = (lo + hi)/2;
		if(arr[test]<=target){
			lo = test;
		}else{
			hi = test;
		}
	}
	return arr[lo] <= target ? hi : lo;
}

int main(){
	int n, days, budget;
	int *prices;
	cin >> n;
	prices = new int[n];
	for (int i = 0; i < n; ++i)
	{
		cin >> prices[i];
	}

	sort(prices,n);

	cin >> days;
	
	while(days--){
		cin >> budget;
		cout << bsearch(prices, budget, n) << endl;
	}

	return 0;
}