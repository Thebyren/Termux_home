#include<iostream>
using namespace std;
int main(){
	int num, y=1, z=1, x=0;
	printf("\n\n\t[SERIE DE FIBONACCI]\n\n");
	do{cout<<"ingrese el valor: "; cin>>num;
	}while(num<0);
	for(int i=1; i<=num; i++ ){
		z= y + x;
		cout<<z<<" ";
		x= y;
		y= z;
	}
	return 0;
}
