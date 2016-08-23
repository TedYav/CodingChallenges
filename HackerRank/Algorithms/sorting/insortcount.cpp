#include <iostream>
#include <vector>

using namespace std;

void insort(vector<int> arr){
	int tmp, count = 0;
	for(vector<int>::iterator s = arr.begin(), e = arr.end(); s < e-1; ++s){
		if(*s > *(s+1)){
			tmp = *(s+1);
			*(s+1) = *s;
			count++;
			for(vector<int>::reverse_iterator rs(next(s,1)), re = arr.rend() - 1; rs < re + 1; ++rs){
				*rs = *(rs + 1) > tmp ? *(rs + 1) : tmp;
				if(*rs == tmp){
					break;
				}
				count++;
			}
		}
	}
	cout << count << endl;
}

int main(){
	int n;
	vector<int> arr;
	cin >> n;
	for(int i=0, t=0; i<n; ++i){
		cin >> t;
		arr.push_back(t);
	}
	insort(arr);
}