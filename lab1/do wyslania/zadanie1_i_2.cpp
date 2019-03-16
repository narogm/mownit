#include <iostream>
#include <ctime>
#include <vector>
#include <fstream>

using namespace std;

const int N = 10000000;

float simple_sum(float* tab){
    float result=0;
    for(int i=0; i<N; i++)
        result += tab[i];
    return result;
}

float recursive_sum(float* tab, int left, int right){
    if(left == right){
        return tab[left];
    }
    int mid = (left+right)/2;
    return recursive_sum(tab,left,mid) + recursive_sum(tab,mid+1,right);
}

float kahan_sum(float* tab){

    float sum = 0.0f;
    float err = 0.0f;
    for (int i = 0; i < N; ++i) {
        float y = tab[i] - err;
        float temp = sum + y;
        err = (temp - sum) - y;
        sum = temp;
    }
    return sum;
}

float blad_bezwzgledy(float real_result,float value){
    return real_result-value;
}

float blad_wzgledny(float real_result,float value){
    return (real_result-value)/real_result;
}

void wykres_bledu(vector <float> &dane,float* tab){
    float result=0;
    for(int i=0; i<N; i++){
        if(i%25000==0)
            dane.push_back(result);
        result += tab[i];
    }
}

int main(){

    float value=0.53125;
    //float value2 = 0.00035;
    float* tab = new float[N];
    for(int i=0; i<N; i++){
        tab[i] = value;
        //i++;
        //tab[i]=value2;
    }

    float real_result = value*N; //(value+value2) * N/2;

    clock_t start = clock();
    float simple_sum_result = simple_sum(tab);
    double simple_sum_time = clock() - start;

    start = clock();
    float recursive_result = recursive_sum(tab,0,N-1);
    double recursive_time = clock() - start;

    start = clock();
    float kahan_result = kahan_sum(tab);
    double kahan_time = clock() - start;

    cout << "dodawanie iteracyjne:\n";
    cout << "dlogosc pomiaru: " << simple_sum_time/CLOCKS_PER_SEC << endl;
    cout << simple_sum_result << endl;
    cout << "blad bezwzgledny: " << blad_bezwzgledy(real_result,simple_sum_result) << endl;
    cout << "blad wzgledny: " << blad_wzgledny(real_result,simple_sum_result) <<endl;

    cout << "\ndodawanie rekurencyjne:\n";
    cout << "dlugosc pomiaru: " << recursive_time/CLOCKS_PER_SEC << endl;
    cout << recursive_result <<endl;
    cout << "blad bezwzgledny: " << blad_bezwzgledy(real_result,recursive_result) << endl;
    cout << "blad wzgledny: " << blad_wzgledny(real_result,recursive_result) <<endl;

    cout << "\ndodawanie algorytmem kahana:\n";
    cout << "dlugosc pomiaru: " << kahan_time/CLOCKS_PER_SEC << endl;
    cout << kahan_result <<endl;
    cout << "blad bezwzgledny: " << blad_bezwzgledy(real_result,kahan_result) << endl;
    cout << "blad wzgledny: " << blad_wzgledny(real_result,kahan_result) <<endl;

    vector <float> dane;
    wykres_bledu(dane,tab);

    ofstream plik;
    plik.open ("example.txt");

    for(int i=0;i<dane.size();i++)
        plik << 25000*i << " " << blad_wzgledny(25000*i*value,dane[i]) << endl;
    plik.close();
}
