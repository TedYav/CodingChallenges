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
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int* readLine(){
	string line;
	getline(cin, line);
	stringstream ss(line);
	int* ret = new int[2];
	ss >> ret[0] >> ret[1];
	return ret;
}

int main(){
	int* line = readLine();
	int n=line[0], q=line[1];

	// stylistic optimization: combine switch below
	// Options 2 and 3 are basically the same.
	// they could be merged.

	int unread = 0;
	
	// size n+1 because first vector is master list
	// using vector of vectors because first list will be all notifications
	vector< vector<bool*> > nList(n+1);
	vector<int> guaranteedRead(n+1) ;
	nList[0]

	for(int i=1; i<n+1; i++){
		nList[i] = vector<bool*>();
		guaranteedRead[i] = 0;
	}

	for(int i=0; i<q; i++){
		line = readLine();
		switch(line[0]){
			case 1: {
				// create a new event
				bool *event = new bool;
				*event = true;
				
				// add to app history
				nList[line[1]].push_back(event);
				
				// add to master history
				nList[0].push_back(event);

				// increase unread count
				unread++;
				break;
			// note: can combine these into 1
			// using cascading switch
			// don't care
			}
			case 2:
				// iterate through app list
				for(int j=guaranteedRead[line[1]]; j<nList[line[1]].size(); j++){
					if(*nList[line[1]][j]){
						*nList[line[1]][j] = false;
						unread--;
					}
				}
				guaranteedRead[line[1]] = nList[line[1]].size();
				break;
			case 3:
				// iterate through master list
				for(int j=guaranteedRead[0]; j<line[1]; j++){
					if(*nList[0][j]){
						*nList[0][j] = false;
						unread--;
					}
				}
				guaranteedRead[0] = line[1];
				break;
		}
		cout << unread << '\n';
	}

	return 0;
}