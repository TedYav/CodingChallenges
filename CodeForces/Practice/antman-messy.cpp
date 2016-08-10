#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

// going to write greedy solution first


//7 4 3
//8 11 12 16 17 18 20
//17 16 20 2 20 5 13
//17 8 8 16 12 15 13
//12 4 16 4 15 7 6
//8 14 2 11 17 12 8
string* data;
int current = 0;

void init(){
    data = new string[6];
    data[0] = "7 4 3";
    data[1] = "8 11 12 16 17 18 20";
    data[2] = "17 16 20 2 20 5 13";
    data[3] = "17 8 8 16 12 15 13";
    data[4] = "12 4 16 4 15 7 6";
    data[5] = "8 14 2 11 17 12 8";
}

string getNext() {
    if(current == 0){
        init();
    }
    return data[current++];
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

void printData(int n,int s,int e,int* x,int* a,int* b,int* c,int* d, int* soln, int* solnVerify){
    cout << "N: " << n << "\tS: " << s << "\tE: " << e << endl;
    string varNames [] = {"x", "a", "b", "c", "d", "soln", "solnVerify" };
    int* vars [] = {x, a, b, c, d, soln, solnVerify};
    for(int j = 0; j<7; j++){
        cout << varNames[j] << ": \t";
        for(int i=0; i<n; i++){
            cout << vars[j][i];
            if(i < n-1){
                cout << ",\t";
            }else{
                cout << endl;
            }
        }
    }
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

    // to verify chair order
    int* solnVerify = new int[n];
    solnVerify[0] = s;

    // s == start
    // e == e

    // 0 indexing fix
    s--;
    e--;

    int currentChair = s;
    int nextChair = -1;
    visited[currentChair] = -1;
    int minTime = 2000000001;
    int curTime = 0;
    for(int i=1; i<n;i++){
        for(int j=0; j<n; j++){
            // can only be end chair on last iteration
            if( (j==currentChair) || (j==e && i != n-1) || (visited[j] == -1)){
                continue;
            }
            curTime = abs(x[j], x[currentChair]) + ((j < currentChair) ? (c[currentChair] + b[j]) : (d[currentChair] + a[j]));
            // cout << "ABS: " << abs(x[j], x[currentChair]) << endl;
            // cout << "CURRENT TIME: " << curTime << " TARGET CHAIR: " << j + 1 << " MIN TIME: " << minTime << endl;
            if(curTime < minTime){
                minTime = curTime;
                nextChair = j;
            }
        }

        soln[i] = soln[i-1] + minTime;

        // update currentChair
        currentChair = nextChair;

        // for verification purposes with 0 indexed fix
        solnVerify[i] = currentChair + 1;

        // mark chair as visited
        visited[currentChair] = -1;

        // reset variables
        minTime = 2000000001;   
        nextChair = -1;
    }

    // fix 0 indexing issue
    s++;
    e++;

    // printData(n,s,e,x,a,b,c,d,soln,solnVerify);
    
    return 0;
}


//int main()
//{
//    int n; cin>>n;
//    int f[100001]; for(int i=0;i<100001;i++) f[i] = -100000;
//    for(int i=0;i<n;i++)
//    {
//        int x, y;
//        cin>>x>>y;
//        int r = 0;
//        for(int j=1;j*j<=x;j++)
//        {
//            if(x%j==0)
//            {
//                int p = x/j;
//                int q = j;
//                if(f[p]<i-y)
//                    r++;
//                f[p] = i;
//                if(f[q]<i-y)
//                    r++;
//                f[q] = i;
//            }
//        }
//        cout<<r<<endl;
//    }
//    return 0;
//
//}