#include<iostream>
using namespace std;

int n, t[INT_MAX];

void build( int v, int tl, int tr, int a[]){
    if(tl == tr){
        t[v]= a[tr];
    }
    else{
        int tm = (tl + tr)/2;
        build(v*2, tl, tm, a);
        build(v*2 +1, tm+1, tr, a);
        t[v]= t[v*2] + t[v*2 + 1];
    }
}

int sum(int v, int tl, int tr, int l, int r){
    if(l == tl && r == tr)
        return t[v];

    if(l > r)
        return 0;

    int tm = (tl + tr)/2;
    return sum(v*2, tl, tm, l, min(tm,r)) + sum(v*2 + 1, tm+1, tr, max(l,tm+1), r);

}

void update(int v, int tl, int tr, int pos, int val){
    if(tr == tl){
        t[v]= val;
    }
    else{
        int tm= (tl + tr) / 2;
        if(pos > tm)
            update(v*2 + 1, tm+1, tr, pos, val);
        else
            update(v*2, tl, tm, pos, val);
        t[v]= t[v*2] + t[v*2 +1];
    }

}

int main(){
    build(1, 0, n-1, a);
    sum(1, 0, n-1, l, r);
    update(1, 0, n-1, pos, val);
}
