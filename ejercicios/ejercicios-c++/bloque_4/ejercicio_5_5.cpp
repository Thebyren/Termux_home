#include<iostream>
using namespace std;
int main(){
	int num, suma=0, negativos=0;
	do{
	cout<<"ingrese su numero; ";
	cin>>num;
	if(num>0){
		suma+=num;
	}
	if(num<0){	
		negativos+=num;
	}
	}while(((num<=20) || (num>=30)) && (num!=0));
	
	cout<<"la suma de los positivos es: "<<suma<<endl;
	cout<<"la duma de los negativos es: "<<negativos<<endl;	
	
	return 0;
}	

