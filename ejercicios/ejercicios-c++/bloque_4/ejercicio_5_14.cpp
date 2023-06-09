#include<iostream>
#include<stdlib.h>
#include<time.h>
using namespace std;
int main(){
	int num, nRandom, contador=0;
	srand(time(NULL));
	nRandom= 1+rand()%(100);
	printf("\n\n\t[INTENTA ADIVINAR EL NUMERO ALEATORIO]\n");
	do{
		cout<<"\ndigita tu numero: ";
		cin>>num;
		if(num != nRandom){
			contador+=1;
		}
		if(num>nRandom){
			cout<<"\nIntenta con un numero menor \n";

		}
		if(num<nRandom){
			cout<<"\nIntenta con un numero mayor\n";

		}
	}while(num!=nRandom);
	cout<<"has tardado "<<contador<<" intentos  en adivinar.";
	return 0;
}
