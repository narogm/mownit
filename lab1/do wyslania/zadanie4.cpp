#include <iostream>
#include <fstream>
#include <vector>
#include <numeric>
#include <limits>
#include <float.h>

using namespace std;

vector<int> iteration_counter_till_zero(vector <float> x_values){
    float r=4;
    vector <int> counters;
    for(int i=0;i<x_values.size();i++){
       float x=x_values[i];
       int counter=0;
       while(x>=FLT_EPSILON){
            x=x*r*(1.0-x);
            counter++;
       }
       counters.push_back(counter);
    }
    return counters;
}

int main(){
    vector <float> x_values;
    x_values.push_back(0.29365);
    x_values.push_back(0.34554);
    x_values.push_back(0.5);
    x_values.push_back(0.44343);
    x_values.push_back(0.82345);
    x_values.push_back(0.17134);
    vector <int> counters;
    counters = iteration_counter_till_zero(x_values);
    for(int i=0;i<x_values.size();i++)
        cout<<x_values[i]<<"  "<<counters[i]<<endl;
}
