#include <bits/stdc++.h>
#include <cstdio>
#include <cstdlib>
using namespace std;

// const double ax0=-0.0008566850547577447,ay0=-0.0007844198694559001;
const double ax0=0,ay0=0;
double ax[10000],ay[10000],w[10000],ta[10000],tw[10000];
double x[10000],y[10000];
double vx,vy,dta,dtw,wjf,lx,ly;
int len1,len2,j;
string temp;

int main(){
    memset(x,0,sizeof(x));
    memset(y,0,sizeof(y));

    freopen("out.txt","w",stdout);

    freopen("FAccelerometer.csv","r",stdin);
    getline(cin,temp);
    while(cin>>ta[len1++]>>ax[len1]>>ay[len1]>>temp){}
    len1-=2;
    //Todo: Check out why the last number wasn't read.
    //      Now just modify len1 to let it looks right.
    fclose(stdin);
    freopen("FGyroscope.csv","r",stdin);
    cin.clear();
    getline(cin,temp);
    while(cin>>tw[len2++]>>temp>>temp>>w[len2]){}
    len2--;
    fclose(stdin);
    
    vx=vy=j=wjf=0;
    dtw=tw[1]-tw[0];
    wjf=w[0]*dtw;
//     double ave=0,sum=0;
//     for (int i=0;i<len1;i++){
//         sum+=ax[i];
//     }
//     ave=sum/len1;
    for (int i=0;i<len1;i++){
        ax[i]-=ax0;
        // printf("%lf\n",ax[i]);
    }
// // cout<<endl<<endl<<"========"<<endl<<endl;
//     sum=0;
//     ave=0;
//     for (int i=0;i<len1;i++){
//         sum+=ay[i];
//     }
//     ave=sum/len1;
    for (int i=0;i<len1;i++){
        ay[i]-=ay0;
        // printf("%lf\n",ay[i]);
    }

    for (int i=0;i<len1;i++){
    // for (int i=0;i<10;i++){
        while (ta[i]>tw[j]){
            j++;
            dtw=tw[j+1]-tw[j];
            wjf+=w[j]*dtw;
        }
        dta=ta[i+1]-ta[i];
        x[i]=x[i-1]+vx*cos(wjf)*dta-vy*sin(wjf)*dta;
        y[i]=y[i-1]+vx*sin(wjf)*dta+vy*cos(wjf)*dta;
        vx+=ax[i]*dta;
        vy+=ay[i]*dta;
        x[i]+=vx*cos(wjf)*dta*dta*0.5-vy*sin(wjf)*dta*dta*0.5;
        y[i]+=vx*sin(wjf)*dta*dta*0.5+vy*cos(wjf)*dta*dta*0.5;
        // printf("%.4lf %.4lf i=%d,j=%d \n  vx=%.4lf,vy=%.4lf w=%.4lf\n",x[i],y[i],i,j,vx,vy,w[j]);
        printf("%lf %lf\n",x[i],y[i]);
    }
    return 0;
}