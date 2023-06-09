#include<iostream>
using namespace std;

int main(){
	char array1[4]={'hola'};
	char array2[5]={'mundo'};
	char array3[10];
	array3[10]=array1,array2;
	cout<<array3;	

	return 0;
}
