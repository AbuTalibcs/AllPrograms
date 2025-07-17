//Program for matrix
#include <iostream>
using namespace std;

int main(){
	
	int row, col;
	int matrix[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
	int arr[row][col];
	int sum[row][col];
	
	cout<<"Enter the number of rows: "<<endl;
	cin>>row;
	cout<<"Enter the number of colums: "<<endl;
	cin>>col;
	cout<<"Enter the elements of matrix: "<<endl;
	
	for(int i=0;i<row; i++){
		for(int j=0; j<col;j++){
			cin>>arr[i][j];
			
		}
		
	}
	cout <<"The Matrix is "<<endl;
	for(int i=0;i<row; i++){
		for(int j=0; j<col;j++){
			cout<<arr[i][j]<<endl;
			
		}
		
	}
	cout<<"The Matrix 2 is "<<endl;
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			cout<<matrix[i][j]<<endl;
		}
	}
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			
			sum[i][j] = arr[i][j] + matrix [i][j];
		}
	}
	cout<<"The sum of both Matrix is "<<endl;
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			cout<<sum[i][j]<<endl;
		}
	}
	

		
	return 0;
}
