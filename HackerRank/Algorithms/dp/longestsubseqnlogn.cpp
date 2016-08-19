#include <iostream>
#include <climits>

inline int binsearch(int arr[], int target, int len){
	int hi = len+1, lo = 0, test;
	while(hi-lo > 1){
		test = (hi+lo)/2;
		if(arr[test] >= target){
			hi = test;
		}else{
			lo = test;
		}
	}
	return lo;
}

int main(){
	std::ios::sync_with_stdio(false);

	int n, a[1000005], l[1000005], longest=0, pos;

	std::cin >> n;

	l[0] = -1;
	l[1] = INT_MAX;

	for (int i = 0; i < n; ++i){
		std::cin >> a[i];
		l[i+2] = INT_MAX;
		pos = binsearch(l, a[i], longest);
		l[pos+1] = a[i];
		if(pos + 1 > longest){
			longest = pos + 1;
		}
	}

	std::cout << longest << std::endl;
	return 0;
}