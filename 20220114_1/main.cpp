#include <bits/stdc++.h>
#include <cstdio>
#include <cstdlib>
using namespace std;

double ax[10000],ay[10000],w[10000],ta[10000],tw[10000];
int len1,len2;
string temp;

int main(){
    freopen("FAccelerometer.csv","r",stdin);
    getline(cin,temp);
    while(cin>>ta[len1++]>>ax[len1]>>ay[len1]>>temp){}
    fclose(stdin);
    freopen("FGyroscope.csv","r",stdin);
    cin.clear();
    getline(cin,temp);
    getline(cin,temp);
    while(cin>>tw[len2++]>>temp>>temp>>w[len2]){}
    fclose(stdin);
    
    return 0;
}