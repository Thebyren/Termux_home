#include<iostream>
using namespace std;
int main(){
	float temperatura, mayor=0, menor=999, media=0;
	for(int i=0; i<24; i+= 4){
		cout<<"ingrese la temperatura: ";
		cin>>temperatura;
		if(temperatura>mayor){
			mayor=temperatura;
		}
		if(temperatura<menor){
			menor=temperatura;
		}
		media+=temperatura;
	}
	media=media/6;
	cout<<"\nla temperatura mas alta fue: "<<mayor<<endl;
	cout<<"la temperatura mas baja fue: "<<menor<<endl;
	cout<<"el promedio del dia fue: "<<media<<endl;

	return 0;
}
