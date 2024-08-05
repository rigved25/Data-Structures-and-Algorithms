#include<bits/stdc++.h>
#define ll long long int
using namespace std;

int main(){
    int T, N, Q, L, R;
    string in;
    cin>>T;
    for(int t=1; t<=T; t++){
        cin>>N>>Q;
        cin>>in;
        int freq[N+1][26] = {0};
        for(int i=1; i<=N; i++){
            freq[i][in[i-1] - 'A']++;
        }

        for(int i=1; i<=N; i++){
            for(int j=0; j<26; j++){
                freq[i][j] += freq[i-1][j];
            }
        }

        int cnt = 0, loc;
        for(int i=0; i<Q; i++){
            cin>>L>>R;
            loc = 0;
            for(int j=0; j<26; j++){
                if((freq[R][j] - freq[L-1][j]) > 0 && ((freq[R][j] - freq[L-1][j]) % 2)){
                    loc++;
                    //cout<<"l: "<<L<<" r: "<<R<<endl;
                }

            }
            if(loc <= 1)
                cnt++;
        }
        cout<<"Case #"<<t<<": "<<cnt<<endl;
    }

}
