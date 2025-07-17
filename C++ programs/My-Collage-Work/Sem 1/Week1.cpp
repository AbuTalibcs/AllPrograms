//WAP in C++ to find factorial of a given number.
#include <iostream>
using namespace std;

int main(){

    int n, fact=1;
    cout<<"Enter a number: ";
    cin>>n;

   if(n>=0){

     for(int i=1; i<=n; i++){
        
            fact *=i;
     
        }
     cout<<"Factorial of "<<n<<" is "<<fact<<endl;

    }
    else{

      cout<<"Please enter a Positive Number!\n";

    }    

    return 0;

}