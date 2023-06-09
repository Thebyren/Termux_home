#include<iostream>
using namespace std;
int main(){
	int num, resultado=0,modulo=0;
	do{
	printf("\tSUMAR PARES, RESTAR PARES\n");
	cout<<"ingrese su valor: ";
	cin>>num;
	}while(num<0);
	for(int i=0; i<=num; i++){
		if(i%2==0){
			resultado-=i;
		}
		else if(i%2!=0){
			resultado+=i;
		}
	}
	cout<<"el resultado de "<<num<<" es "<<resultado;
	return 0; 
}
