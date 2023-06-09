#include<iostream>
using namespace std;

int main(){
	int lista[5] = {1,2,3,4,5};
	int producto=1;
	for(int i=0; i<5; i++){
		producto*=lista[i];
		cout<<producto<<endl;
	}
	cout<<" resultado final: "<<producto<<endl;

 return 0;
}
