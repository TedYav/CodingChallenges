/*

	By TEOMAN (TED) YAVUZKURT
	www.teomandavid.com
	hello@teomandavid.com

	PROBLEM: http://codeforces.com/problemset/problem/704/A
	SOLUTION:

	This solution was inspired by others on here. At first, I was using
	vectors of boolean pointers as I'm not super familiar with C++ and that seemed
	to be a smart way to do it, as editing the boolean pointer in one place
	would cause it to change in another.

	This approach is smarter. It keeps offset counts as well as raw counts for each app.

	It then uses these to calculate unread notifications per app.

	Thus it's mathematical, rather than relying on large memory allocation
	and pointers, which are slower.

*/

/*
#include<iostream>
using namespace std;
int n, q, k, v, x, y, t, a[300300], b[300300], c[300300];
int main() {
	cin >> n >> q;
	while (q--) {
		cin >> k >> v;
		if (k == 1) a[++y] = v, b[v]++, c[v]++, t++;
		else if (k == 2) t -= b[v], b[v] = 0;
		else while (x < v) { c[a[++x]] ? c[a[x]]-- : 0; b[a[x]]>c[a[x]] ? t--, b[a[x]]-- : 0; }
		cout << t << endl;
	}
}
*/

#include <iostream>

using namespace std;

int main(){
	int n, q, event=0, arg=0, unread=0, totalevents=0, offset=0, allevents[300300], appcounts[300300], appoffsets[300300];

	cin >> n >> q;

	while(q--){
		cin >> event >> arg;
		if(event == 1){
			unread++;
			allevents[++totalevents] = arg;
			appcounts[arg]++;
			appoffsets[arg]++;
		}else if(event == 2){
			unread -= appcounts[arg];
			appcounts[arg] = 0;
		}else{
			while(offset < arg){
				// if it's nonzero offset, then it means we haven't observerd these events
				// while iterating through the big list

				// that said, only the last few of them, if any, may actually be unread
				// so we check

				if(appoffsets[allevents[++offset]]){
					appoffsets[allevents[offset]]--;
				}

				// check if the unread count for this app is greater than the amount we
				// haven't observed while iterating through the list

				// this means this must be an unread notification
				if(appcounts[allevents[offset]] > appoffsets[allevents[offset]]){
					appcounts[allevents[offset]]--;
					unread--;
				}
			}
		}
		cout << unread << endl;
	}

	return 0;
}