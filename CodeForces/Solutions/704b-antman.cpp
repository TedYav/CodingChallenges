/*

    704B: Antman

    PROBLEM: http://codeforces.com/problemset/problem/704/B

    SOLUTION:

*/

#include <iostream>
#include <string>
#include <sstream>

using namespace std;

string getNext() {
    string line;
    getline(cin, line);
    return line;
}

int* populate(int n){
    int* target = new int[n];
    string line = getNext();
    stringstream ss(line);
    for(int i=0; i<n; i++){
        ss >> target[i];
    }
    return target;
}

int abs(int a, int b){
    int result = a - b;
    if(result < 0){
        result *= -1;
    }
    return result;
}

int main() {
    int* t = populate(3);
    int n = t[0], s = t[1], e = t[2];
    int* x = populate(n);
    int* a = populate(n);
    int* b = populate(n);
    int* c = populate(n);
    int* d = populate(n);

    int* visited = new int[n];
    for(int i=0; i<n; i++){
        visited[i] = 1;
    }
    
    int* soln = new int[n];
    soln[0] = 0;

    s--;
    e--;

    int currentChair = s;
    int nextChair = -1;
    visited[currentChair] = -1;
    int minTime = 2000000001;
    int curTime = 0;
    for(int i=1; i<n;i++){
        for(int j=0; j<n; j++){
            if( (j==currentChair) || (j==e && i != n-1) || (visited[j] == -1)){
                continue;
            }
            curTime = abs(x[j], x[currentChair]) + ((j < currentChair) ? (c[currentChair] + b[j]) : (d[currentChair] + a[j]));
            if(curTime < minTime){
                minTime = curTime;
                nextChair = j;
            }
        }

        soln[i] = soln[i-1] + minTime;

        // update currentChair
        currentChair = nextChair;

        // mark chair as visited
        visited[currentChair] = -1;

        // reset variables
        minTime = 2000000001;   
        nextChair = -1;
    }

    cout << soln[n-1];
    
    return 0;
}