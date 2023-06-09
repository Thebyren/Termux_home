#include<iostream>
using namespace std;

int main(){
	int a, numeros[100];
		cout<<"inserte el numero de elementos: ";
		cin>>a;
	for(int i=0; i<a; i++){
		cout<<"inserte el elemento: ";
		cin>>numeros[i];
	}
	for(int i=0; i<a; i++){
		cout<<i<<" es indice de: "<<numeros[i]<<endl;
	}


	return 0;
}
