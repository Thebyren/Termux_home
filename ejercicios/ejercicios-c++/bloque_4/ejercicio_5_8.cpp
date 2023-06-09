#include<iostream>
using namespace std;
int main(){
        int num, resultado=0;
        cout<<"\n\n\tINGRESE SU VALOR\n\n";
        cout<<"ingrese su numero: "; cin>>num;                     
        if(num>0){
        for(int i=1; i<=2*num-1; i+=2){
		resultado+=i;
        }                                                                  cout<<"su resultado es: "<<resultado<<endl;
        }

        else{
        cout<<"su resultado es imposible de calcular"<<endl;               }

        return 0;
}
