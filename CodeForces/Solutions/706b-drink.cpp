#include <iostream>
#include <random>
using namespace std;

void swap(int arr[], int a, int b){
	int temp = arr[b];
	arr[b] = arr[a];
	arr[a] = temp;
}

void sort(int arr[], int length){
	if(length > 1){
		int offset = 0;
		for(int i=0; i<length; i++){
			if(arr[i]<arr[length-1]){
				swap(arr,offset++,i);
			}
		}
		swap(arr, offset++,length-1);
		sort(arr, offset - 1);
		sort(arr+offset, length-offset);
	}
}

void testSort(int size, int num){
	int* arr = new int[size];
	random_device rd;
	mt19937 eng(rd());
	uniform_int_distribution<> distr(-1*size,size);
	bool success = true;
	for(int j=0; j<num; j++){
		for (int i = 0; i < size; i++)
		{
			arr[i] = distr(eng);
		}
		sort(arr,size);
		success = true;
		for (int i = 0; i < size-1; i++)
		{
			if(arr[i] > arr[i+1]){
				cout << "FAILURE: " << arr[i] << " > " << arr[i+1] << endl;
				success = false;
			}
		}
		cout << "TEST " << j << ((success) ? " PASSED" : " FAILED") << endl;
	}
}

/*
std::random_device rd; // obtain a random number from hardware
    std::mt19937 eng(rd()); // seed the generator
    std::uniform_int_distribution<> distr(25, 63); // define the range

    for(int n=0; n<40; ++n)
        std::cout << distr(eng) << ' '; // generate numbers
*/

int main(){
	testSort(5000000,5000);
	return 0;
}