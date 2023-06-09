#include<iostream>
using namespace std;

int main(){
	int numeros[100], a;
		cout<<"ingrese el numero de elementos: ";
		cin>>a;
	for(int i=0; i<a; i++){
		cout<<"ingrese el valor del elemento: ";
		cin>>numeros[i];
	}

	cout<<"\torden ascendente\n\n";
	for(int i=0; i<a; i++){
		cout<<i<<" indice de: "<<numeros[i]<<endl;
	}

	cout<<"\torden desendente\n\n";
	for(int i=a-1; i>=0; i--){
		cout<<i<<" indice de: "<<numeros[i]<<endl;
	}


	return 0;
}
