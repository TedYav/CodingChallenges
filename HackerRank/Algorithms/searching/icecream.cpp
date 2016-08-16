#include <iostream>
#include <vector>
#include <algorithm>

// could accelerate by sorting
// and binary searching
// but not needed here

using namespace std;

struct kvpair{

	short index;
	short val;
};

bool compkvpair(kvpair a, kvpair b){
	return a.val < b.val;
}

int main(){
	int t, n, m, a, b;
	vector<kvpair> p;
	short tmp;
	cin >> t;
	while(t--){
		cin >> m >> n;
		a = 0;
		b = 0;

		p = vector<kvpair>();

		for (short i = 0; i < n; ++i){
			cin >> tmp;
			if(tmp < m){
				kvpair c = kvpair();
				c.index = i + 1;
				c.val = tmp;
				p.push_back(c);
			}
		}
		sort(p.begin(), p.end(), compkvpair);

		for (vector<kvpair>::iterator s = p.begin(), e = p.end(); s!=e; ++s){
			for(vector<kvpair>::reverse_iterator rs = p.rbegin(), re = p.rend(); rs != re; ++rs){
				if(s->val + rs->val <= m){
					if(s->val + rs-> val == m){
						a = s->index;
						b = rs->index;
					}
					break;
				}
			}
			if(a != 0){
				if(a > b){
					a = a ^ b;
					b = b ^ a;
					a = a ^ b;
				}
				break;
			}
		}
		cout << a << " " << b << endl;
	}
	return 0;
}