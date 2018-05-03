//
//  bayes.cpp
//  
//
//  Created by Nicolas Felipe Vergara Duran on 3/05/18.
//
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <math.h>
using namespace std;
double* linspace(double in, double end, int size){
    double* vector = new double[size];
    double h=(end-in)/(size-1);
    double point=in;
    for(int i=0;i<size;i++){
        vector[i]=point;
        point+=h;
    }
    return vector;
}
void probabilidad(){
    double* lambda=linspace(0,100,200);
    double* Normalizacion=1/(exp(-(1/lambda)))
}
