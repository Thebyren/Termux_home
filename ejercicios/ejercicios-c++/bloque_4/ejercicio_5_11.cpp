#include<iostream>
#include<iostream>
using namespace std;
int main(){
	int num, resultado=1, resultado1=0;
	cout<<"ingrese el su numero: "<<endl;
	cin>>num;
	for(int i=1; i<=num; i++){
		resultado= pow(2,i);
		resultado1+=resultado;
	}
	cout<<"el resultado de "<<num<<" es: "<<resultado1<<endl;

	return 0;
}
