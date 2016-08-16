#include <iostream>
#include <limits>

using namespace std;

int max(int a, int b){
	return a > b ? a : b;
}

int arrmax(int arr[], int size){
	// really int min not defined??
	int m = -99999;
	for (int i = 0; i < size; ++i){
		m = arr[i] > m ? arr[i] : m;
	}
	return m;
}

int main(){
	int t, n, *arr, *mc, *m;
	cin >> t;
	while(t--){
		cin >> n;
		arr = new int[n];
		
		for (int i = 0; i < n; ++i){
			cin >> arr[i];
		}

		mc = new int[n];
		m = new int[n];
		mc[0] = m[0] = arr[0];
		
		for (int i = 1; i < n; ++i){
			mc[i] = max(mc[i-1] + arr[i], arr[i]);
			m[i] = max(max(m[i-1] + arr[i], m[i-1]),arr[i]);
		}
		cout << arrmax(mc,n) << " " << arrmax(m,n) << endl;
	}
	return 0;
}