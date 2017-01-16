#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, totalDiff = 0, partialDiff = 0, result = -1;
    cin >> n;
    vector<int> x(n);
    vector<int> y(n);
    for (int i = 0; i < n; ++i)
    {
    	cin >> x[i];
    }
    for (int i = 0; i < n; ++i)
    {
    	cin >> y[i];
    	totalDiff += x[i] - y[i];
    	partialDiff += x[i] - y[i] > 0 ? x[i] - y[i] : 0;
    }
    result = totalDiff == 0 ? partialDiff : -1;
    cout << result;
    return 0;
}
