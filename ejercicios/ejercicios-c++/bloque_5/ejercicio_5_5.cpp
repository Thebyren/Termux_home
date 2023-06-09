#include<iostream>
using namespace std;

int main(){
	int MAX, array[100],large ;
	cout<<"cuantos vectores quiere: ";
	cin>>large;
		for(int i=0; i<large; i++){
			cout<<"ingrese el valor de un vector: " ;
			cin>>array[i];
			if(MAX<array[i]){
				MAX=array[i];
			}
		}
	cout<<"El valor maximo del array es: "<<MAX<<endl;
	


	return 0;
}
