//program to find uique number in an array
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	 
	int arr[9] = {2,5,4,8,8,5,2,3,3};
	int n = sizeof(arr) / sizeof (arr[0]);
	
	sort(arr, arr + n);
	
	for(int i =0; i<9; i++){
		cout<<arr[i]<<endl;
	// New Array { 2 2 3 3 4 5 5 8 8 }	
	}
	
	for(int i = 0; i<9; i+=2){
		if(arr[i] != arr[i+1]){
		cout<<"The unique number is "<<arr[i]<<endl;
	}
		
	}
	
	return 0;
}

