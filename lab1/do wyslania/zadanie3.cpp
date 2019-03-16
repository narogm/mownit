#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

double dzeta_forward(float s, int n){
    double result = 0;
    for(int i=1; i<=n; i++)
        result += 1/pow(i,s);
    return result;
}

double dzeta_backward(float s, int n){
    double result = 0;
    for(int i=n;i>0;i--)
        result += 1/pow(i,s);
    return result;
}

double eta_forward(float s,int n){
    double result = 0;
    for(int i=1;i<=n;i++)
        result += pow((-1),i-1) * (1/pow(i,s));
    return result;

}

double eta_backward(float s, int n){
    double result = 0;
    for(int i=n;i>0;i--)
        result += pow((-1),i-1) * (1/pow(i,s));
    return result;
}

int main(){
    float s = 7.2;
    int n[]={50,100,200,500,1000};

    for(int i=0;i<5;i++){
    cout << "n = " << n[i] <<endl;
    cout << "dzeta forward:\n" << setprecision(25) << dzeta_forward(s,n[i]) << endl;
    cout << "dzeta backward:\n" << dzeta_backward(s,n[i]) << endl << endl;
    }

    for(int i=0;i<5;i++){
    cout << "n = " << n[i] <<endl;
    cout << "eta forward:\n" << eta_forward(s,n[i]) << endl;
    cout << "eta backward:\n" << eta_backward(s,n[i]) << endl;
    cout << endl;
    }
}
