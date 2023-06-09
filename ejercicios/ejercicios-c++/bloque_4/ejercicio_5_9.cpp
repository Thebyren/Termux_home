#include<iostream>
using namespace std;
int main(){
        int num, resultado=1;
        cout<<"\n\n\t[FACTORIALES]\n\n";
        cout<<"ingrese su numero: "; cin>>num;                     
        if(num>0){
        for(int i=1; i<=num; i++){
        resultado*=i;
        }                                                                  cout<<"El factorial de "<<num<<" es: "<<resultado<<endl;
        }

        else{
        cout<<"su resultado es imposible de calcular\n\n"<<endl;               }

        return 0;
}
