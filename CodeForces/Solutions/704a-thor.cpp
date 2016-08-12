/*

	PROBLEM: http://codeforces.com/problemset/problem/704/A
	SOLUTION:


*/

#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <climits>

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
	int totalUnread = 0;

	// int[] counts per app
	// int** --> all notifications

	// optimization
	// do not implement at first
	// vector<int>guaranteedRead --> what position to start at in each list



	int unread = 0;
	
	// size n+1 because first vector is master list
	// using vector of vectors because first list will be all notifications
	vector< vector<bool*> > nList(n+1);

	for(int i=0; i<n+1; i++){
		cout << "INITIALIZING VECTOR " << i << endl;
		nList[i] = vector<bool*>();
	}

	// vector<int*> --> nList --> know size. Set to NULL after one is used.
	// vector<list<int*>> --> appList --> Know number of apps, not number of notifications
	// NEED TO USE NOTIFICATION STRUCT IN BOTH PLACES and maintain pointers
	// this way we can easily zero it and adjust our count

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
				cout << unread << endl;
				break;
			// note: can combine these into 1
			// use cascading switch
			}
			case 2:
				// iterate through app list
				for(int j=0; j<nList[line[1]].size(); j++){
					if(*nList[line[1]][j]){
						*nList[line[1]][j] = false;
						unread--;
					}
				}
				cout << unread << endl;
				break;
			case 3:
				// iterate through master list
				for(int j=0; j<line[1]; j++){
					if(*nList[0][j]){
						*nList[0][j] = false;
						unread--;
					}
				}
				cout << unread << endl;
				break;
			default:
				continue;
		}
	}

	return 0;
}