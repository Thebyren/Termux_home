#include<iostream>
using namespace std;
int main(){
	int dia, mes, año, edad=0;
	char estacion[20]=' ';
	do{
	cout<<"ingresa tu dia, mes y año de nacimiento";
	cin>>dia>>mes>>año;
	edad=año-2022;
		if((dia>1 && dia>31) || (mes<1 && mes>12)(año<1940 && año>2022)){
			printf("\t\n\nDato erroneo\n\n");
		}
	}while(dia>31 || mes>12 || año<1940);
	//primavera
	if(mes>=1 && mes<=12){
		if(mes>=3 && mes<=6){
			estacion="primavera";
		}
		if(mes>=6 && mes<=9){
			estacion="verano";
		}
		if(mes>=9 && mes<=12){
			estacion="otoño";
		}
		if(mes==12 || mes<=3 && mes >=1){
			estacion="invierno";
		}
	}
	printf("\n\tFin del programa\n \ttus resultados son");
	cout<<"tu estacion es: "<<estacion<<endl;
	cout<<"tu edad actual es: "<<edad<<endl;

	return 0;
}
