#include <vector>
#include <list>
#include <iostream>

using namespace std;

// naive solution

int main(){
	int n, arg, k;
	char op;

	list<int> history;
	list<int> sequence;

	cin >> n;
	while(n--){
		// cin >> op;
		// if(op=='+'){
		// 	cin >> arg;
		// }
		op = '+';
		arg = 1;

		if(op=='+'){
			sequence.push_back(arg);
			k = 0;
			if(sequence.size()>=2){
				{
					list<int>::const_iterator i;
					list<int>::const_reverse_iterator j;
					for(i = sequence.begin(), j = sequence.rbegin(); i!= sequence.end(); ++i,++j){
						// cout << "I: " << *i << " J: " << *j << " K: " << k << endl;
						if(*i != *j){
							break;
						}
						k++;
					}
				}
				k = k == 0 ? k : k - 1;
			}
			
			history.push_back(k);
			cout << k << endl;
		}else{
			if(history.size() > 0){ history.pop_back(); sequence.pop_back();}
			k = history.size() > 0 ? history.back() : 0;
			cout << k << endl;
		}
	}
	return 0;
}