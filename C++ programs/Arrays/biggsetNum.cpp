#include <iostream>
using namespace std;

int main(){
	
	int Arr[5];
	cout<<"Enter 5 numbers: "<<endl;
	for (int i=0; i<5; i++){
		cin>>Arr[i];
	}
	int MaxNum = 0;
	
	for (int i=0; i<5; i++){
		
		if(MaxNum < Arr[i]){
			
			MaxNum = Arr[i];
		}
		
	}
	cout<<"The biggest number in Array is "<<MaxNum<<endl;
	
	return 0;
}
