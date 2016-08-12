
#include <iostream>
#include <iomanip>

using namespace std;

double precision = 0.000001;

double abs(double test){
	return (test < 0) ? (-1.0 * test) : test;
}

// this algorithm probably sucks
// in fact it definitely sucks but it'll do for now
double sqrt(double num){
	double lo = 0.0, test, hi = num, result, error;
	int i = 0;
	do{
		test = (hi + lo)/2;
		result = test * test;
		error = result - num;
		if(error > 0){
			hi = test;
		}else{
			lo = test;
		}
		// cout << ++i << ". TEST VAL: " << test << " RESULT: " << result << " ERROR: " << error << endl;
	}while(abs(error)>precision);

	return test;
}

int main(){
	// a,b = coords of home
	// n = second line = # of taxis
	// each add'l line: x, y, v == coordinates of taxi and speed
	int a, b, n, x, y, v;
	double time, distance, min = 10000000;
	cin >> a >> b;
	cin >> n;

	while(n--){
		cin >> x >> y >> v;
		distance = sqrt(((x - a)*(x-a)) + ((y-b)*(y-b)));
		time = distance / v;
		// cout << "DISTANCE: " << distance << " TIME: " << time << endl;
		if(time < min){
			min = time;
		}
	}
	cout << std::setprecision(10) << min << endl;
	return 0;
}