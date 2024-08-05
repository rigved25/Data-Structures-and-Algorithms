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

void rotate90(ll& a, ll& b, ll m, ll n){
    ///cout<<" x: "<<a<<" y: "<<b;
    swap(a,b);
    b=n-b-1;
    ///cout<<" x: "<<a<<" y: "<<b<<endl;
}

ll modd(ll a, ll b){
    return (((a%b) + b)%b);
}

inline ll mod(ll a){
    return (a-MOD*(a/MOD));
}

ll power(ll a, ll b){ll res=1;a=mod(a);while(b>0){if(b&1){res=mod(res*a);b--;}a=mod(a*a);b>>=1;}
	return res;}

int main(){
    ll t=0, n=0, k=0, a, b, c, d, x, y, ans =0;
    string s1, s2;
    cin>>t;
    while(t--){
        cin>>n>>x;
        vector<pair<ll, ll>> arr(n);
        ans = 0;
        for(int i=0; i<n; i++) {
            cin>>a;
            arr[i].first = a;
        }
        for(int i=0; i<n; i++) {
            cin>>b;
            arr[i].second = b;
        }
        arr.push_back({n, x});

        std::sort(arr.begin(), arr.end(), [](const auto& a, const auto& b) {
            return (a.second < b.second) || (a.second == b.second && a.first > b.first);
        });

        d=n;
        for(int i=0; i<n; i++){
            if(arr[i].second < x && d>0) {
                d--;
                ans += x + (min(d, arr[i].first) * arr[i].second);
                d = d - min(d, arr[i].first);
            }
            else {
                break;
            }
        }
        if(d>0)
            ans += d * x;
        cout<<ans<<endl;
    }
}





