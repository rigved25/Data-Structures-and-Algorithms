#include<bits/stdc++.h>
using namespace std;

typedef long long int ll;
const int N = 1e6 + 3;
vector <int > g[N];
ll vis[N];
bool flg;

void dfs(ll u, ll par){
    if(vis[par]==1)
        vis[u]=2;
    else
        vis[u]=1;
    for(ll child : g[u]){
        if(vis[child] != -1){
            if(vis[child]==vis[u])
                flg=1;
            continue;
        }
        dfs(child, u);
    }
}


int main(){

    ll t;
    cin>>t;
    vis[0]=1;
    for(ll k=1; k<=t; k++){
        g[0].clear();
        ll n, m, u, v;
        flg=0;
        cin>>n>>m;
        while(m--){
            cin>>u>>v;
            g[v].push_back(u);
            g[u].push_back(v);
        }

        for(ll i=1; i<=n; i++){
            vis[i]=-1;
        }

        for(ll i=1; i<=n; i++){
            if(vis[i]== -1)
                dfs(i,0);

        }
        cout<<"Scenario #"<<k<<":"<<endl;
        if(flg==1)
            printf("Suspicious bugs found!\n");
        else
            printf("No suspicious bugs found!\n");

    }
}
