#include <iostream>
#include <string>
using namespace std;

class Employee {
private:
    int Password;
public:
    string name;
    string role;
    string branch;
    string adress;
    double slary;
    int age;
    int empId;

Employee(){
    cout<<"Punjab Namtional Bank: \n";
}

};

int main(){

    Employee e1;
 
    cout<<"Enter the details of the employees: \n";

    cout<<"Enter the name of the employees: \n";
    cin>>e1.name;
    cout<<"Enter the adress of the employees: \n";
    cin>>e1.adress;
    cout<<"Enter the age of the employees: \n";
    cin>>e1.age;
    cout<<"Enter the role of the employees: \n";
    cin>>e1.role;

    cout<<"Name : "<< e1.name << endl;
    cout<<"Adsress : "<< e1.adress << endl;
    cout<<"Age : "<< e1.age << endl;
    cout<<"role : "<< e1.role << endl;
    
    return 0;

}