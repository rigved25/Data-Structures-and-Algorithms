/// #pragma GCC optimize("Ofast")
/// #pragma GCC target("avx")
using namespace std;
#define ll long long
/// #include <ext/pb_ds/assoc_container.hpp>
/// #include <ext/pb_ds/tree_policy.hpp>
/// using namespace __gnu_pbds;
/// typedef tree<ll, null_type, less_equal<ll>, rb_tree_tag,tree_order_statistics_node_update>ordered_set;
/// using namespace chrono;
#include<bits/stdc++.h>
#define F first
#define S second
#define lld long double
#define vc vector<ll>
#define pb push_back
#define all(a) a.begin(),a.end()
const int MOD=(1e9 +7);
/// const ll inf=(1000000000000000000);
typedef pair<ll,ll> pairs;
#define varval(...) " [" << #__VA_ARGS__ ": " << (__VA_ARGS__) << "] "
inline ll mod(ll a){
    return (a-MOD*(a/MOD));
}
ll power(ll a, ll b){ll res=1;a=mod(a);while(b>0){if(b&1){res=mod(res*a);b--;}a=mod(a*a);b>>=1;}
	return res;}

#define P 62000
vector<ll> prime(P, 0);
void sieve(){
    for(ll i=4; i<P; i=i+2)
        prime[i]=2;
    for(ll pr=3; pr*pr<P; pr=pr+2){
        if(prime[pr]!=0)
            continue;

        for(ll mu=pr*pr; mu<P; mu+=2*pr){
            if(prime[mu]==0)
                prime[mu]=pr;
        }
    }
}

unordered_map<ll,vector<ll>> adj;
unordered_map<ll, bool> visited;
ll  sender = 0, reciever = 0, totans = 0;
vector<ll> ans;
bool dfs(ll current, ll parent){
    if(current == reciever){
        return true;
    }

    bool a = false;
    for(auto child: adj[current]){
        if(child == parent || visited[child]) continue;

        if(dfs(child, current)){
             a = true;
            if(current == sender){
                totans++;
                ans.push_back(child);
            }
        }

    }
    return a;
}

template<class T>
void display(vector<T> arr){
    for(auto i: arr){
        cout<<i<< " ";
    }
    cout<<endl;
}

int main() {
	std::ios::sync_with_stdio(false);
	//cin.tie(NULL);cout.tie(NULL);
    ll t, N, X, Y, Z, M, K, in, ans, A, B, AB, O;
    string s, name;
    cin>>N;
    while(t--)
    {
        cin>>N>>M>>Y;
        for(ll i=0; i<N; i++){

        }

        printf("%d\n", ans);
    }
    // cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
	return 0;
}
