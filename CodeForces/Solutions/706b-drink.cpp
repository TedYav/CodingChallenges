#include <iostream>
using namespace std;

void swap(int arr[], int a, int b){
	int temp = arr[b];
	arr[b] = arr[a];
	arr[a] = temp;
}

void sort(int arr[], int length){
	if(length <= 1){
		return;
	}

	cout << "SORTING: " << endl;
	for (int i = 0; i < length; i++)
	{
		cout << arr[i] << endl;
	}
	cout << "XXXXXX" << endl;

	int pivot = arr[length-1]; // right pivot

	int offset = 0;
	for(int i=0; i<length; i++){
		if(arr[i]<pivot){
			swap(arr,offset++,i);
		}
	}

	swap(arr,offset++,length-1);

	cout << "PIVOTED: " << endl;
	for (int i = 0; i < length; i++)
	{
		cout << arr[i] << endl;
	}
	cout << "OFFSET: " << offset << endl;
	cout << "XXXXXX" << endl;

	sort(arr, offset - 1);
	sort(arr+offset, length-offset);

	return;
}

int main(){
	int test[] = {2,8,5,4,3,2,4}; // 2,3,4,5,8
	for (int i = 0; i < 5; i++)
	{
		cout << test[i] << endl;
	}
	sort(test, 7);
	for (int i = 0; i < 7; i++)
	{
		cout << test[i] << endl;
	}
	return 0;
}