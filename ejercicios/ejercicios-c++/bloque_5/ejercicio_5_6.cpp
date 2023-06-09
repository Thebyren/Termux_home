#include<iostream>
using namespace std;

int main(){
	int array[4]={1,2,2,5}, suma=0, resultado=0;
	for(int i=0; i<4; i++){
		for(int j=0; j<4; j++){	
			suma+=array[j];
		}
		if(array[i]==suma-array[i]){
		resultado=array[i];
		}
		else{
		suma=0;
		}
	}
	cout<<resultado;





	return 0;
}
