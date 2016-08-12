/*

	By TEOMAN (TED) YAVUZKURT
	www.teomandavid.com
	hello@teomandavid.com

	PROBLEM: http://codeforces.com/problemset/problem/704/A
	SOLUTION:

	There is no pretty way to do this. There are some optimizations
	listed in the code below, but we have to check at least some
	elements each time we iterate.

	We allocate a vector of vectors that will hold our notification
	lists. The first element (0) is the master list. Every other list
	is for a specific app.

	Each notification is a boolean value. True if unread, False if read.

	Each list contains a list of pointers to these boolean values.

	This way, if we set one to false in the master list, it's false in
	the app lists, and vice versa.

	The rest is just a matter of specifying cases.

	FURTHER OPTIMIZATIONS: preallocate initial vector
						   use lists for each->store pointer to beginning
						   instead of guaranteed Read

*/

#include <iostream>

using namespace std;

int main(){
	int n, q, event, arg, unread, totalevents, offset, allevents[300300], appcounts[300300], appoffsets[300300];

	cin >> n >> q;

	while(q--){
		cin >> event >> arg;
		if(event == 1){
			unread++;
			allevents[++totalevents] = arg;
			appcounts[arg]++;
			appoffsets[arg]++;
			cout << "ADDED EVENT TO APP: " << arg;
			cout << " APP COUNT: " << appcounts[arg] << " APP OFFSET: " << appoffsets[arg] << endl;
		}else if(event == 2){
			unread -= appcounts[arg];
			appcounts[arg] = 0;
			cout << "CLEARED EVENTS TO APP: " << arg;
			cout << " APP COUNT: " << appcounts[arg] << " APP OFFSET: " << appoffsets[arg] << endl;
		}else{
			cout << "DELETING " << arg << " EVENTS: " << endl;
			if(offset > arg){
				cout << "OFFSET TOO BIG SKIPPING LOOP " << endl;
			}
			while(offset < arg){
				// if it's nonzero offset, then it means we haven't observerd these events
				// while iterating through the big list

				// that said, only the last few of them, if any, may actually be unread
				// so we check

				if(appoffsets[allevents[++offset]]){
					appoffsets[allevents[offset]]--;
					cout << "EVENT FOR APP: " << allevents[offset] << " NEW OFFSET: " << appoffsets[allevents[offset]] << " RAW COUNT: " << appcounts[allevents[offset]] << endl;
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
		cout << unread << '\n';
	}

	return 0;
}