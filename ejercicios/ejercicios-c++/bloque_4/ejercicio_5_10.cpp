#include<iostream>
using namespace std;
int main(){
	int num, factor1=1, factor2=0;
	printf("\tSUMA DE FACTORIALES\n\n");
	cout<<"ingrese el factorial de factoriales: ";
	cin>>num;
	for(int i=1; i<=num; i++){
		factor1*=i;
		factor2+=factor1;
	}
	cout<<"\nel resultado de "<<num<<" es: "<<factor2<<endl;

	return 0;
}
