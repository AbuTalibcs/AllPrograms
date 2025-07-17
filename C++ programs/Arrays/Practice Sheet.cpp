#include <iostream>
using namespace std;
/*
int main(){
	
	int Arr[15]={0};
	
	Arr[0] = 10;
	Arr[14] = 150;
	
	for (int i=0; i<=14; i++){
		
		cout<<Arr[i]<<endl;
		
	}
	
	return 0;
} */

int main (){
	
	int arr1[5] = {0};
	int arr2[5] = {0};
	int arr3[5] = {0};
	
	cout<<"Enter number in Arr1";
	for(int i=0; i<5; i++){
		
		cin>>arr1[i];
		
	}
	
	cout<<"Enter number in Arr2";
	for(int i=0; i<5; i++){
		
		cin>>arr2[i];
	}
	
	for(int i; i<5; i++){
		
		arr3[i]=arr1[i]+arr2[i];
		
	}
	
	cout<<"Arr1"<<endl;
	for (int i=0; i<=4; i++){
		
		cout<<arr1[i]<<endl;
		
	}
	
	cout<<"Arr2"<<endl;
	for (int i=0; i<=4; i++){
		
		cout<<arr2[i]<<endl;
		
	}
	
	cout<<"Sum of arr1 and arr2";
	for (int i=0; i<=4; i++){
		
		cout<<arr3[i]<<endl;
		
	}
	
	return 0;
}

/*
//public class Solution {
   // public int[] TwoSum(int[] nums, int target) {
   int main(){
   
    int nums[5] = {2,5,8,6,7};
    int  target = 14; 
	  
     for(int i=0 ; i<4; i++){
       for(int j = i+1; j<4; j++){
         if(target ==(nums[i]+nums[j])){
            cout<<i <<" and "<<j <<endl;
         }

       }

     }
   return 0;
    }
*/
