#include<iostream>
using namespace std;
int main(){
	int x, y, resultado;
	cout<<"ingrese el valor de x ";
	cin>>x;
	cout<<"ingrese ek valor de y ";
	cin>>y;
	resultado=x;
	for(int i=1; i<y; i++){
		resultado*=x;
	}
	cout<<"resultado: "<<resultado;
	return 0;
}
