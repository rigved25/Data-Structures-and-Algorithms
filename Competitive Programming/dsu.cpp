#include<bits/stdc++.h>
using namespace std;

vector<int > par,siz;

void make_set(int x){
    par[x]=x;
    siz[x]=1;
}
int find_set(int x){
    if(par[x]==x)
        return x;
    return par[x]=find_set(par[x]);
}
void union_set(int x, int y){
    x=find_set(x);
    y=find_set(y);
    if(x!=y){
        if(siz[x]<siz[y])
            swap(x,y);
        par[y]=x;
        siz[x]+=siz[y];
    }
}

int main(){

}
