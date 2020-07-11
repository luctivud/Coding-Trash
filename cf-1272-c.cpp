/*  Created by: @luctivud  at 2020-07-11 09:56:57  */

// #include "bits/stdc++.h"
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

using namespace std;

const long long int MOD_JOHAN {1000000007};
const long long int MOD_LIGHT {998244353};
const long long int MAXN_EYEPATCH = 1e6 + 1LL;
const long long int MAXN_FULLMETAL = 501LL;

typedef string STR;
typedef long long int lld;
typedef vector<int> v_int;
typedef vector<lld> v_lld;
typedef pair<int, int> p_int;
typedef pair<lld, lld> p_lld;


#define                 GREED_FOR_SPEED   ios_base::sync_with_stdio(false); cin.tie(0)
#define           TESTCASES_ARE_THERE()   lld Test; _scan(Test); while(Test--)
#define                   mems(arr,val)   memset((arr), val, sizeof((arr)))
#define   FORFWD(itr, start, end, step)   for(lld itr = start; itr < end; itr += step)
#define   FORBWD(itr, start, end, step)   for(lld itr = start; itr > end; itr -= step)
#define                            endl   "\n"
#define            FOREACH(___vec, itr)   for(auto itr = ___vec.begin(); itr != ___vec.end(); itr++)
#define                   INPUT(___vec)   for(auto &___vec___itr : ___vec) _scan(___vec___itr)
#define                              PI   3.1415926535897932384626433832795
#define                            INFF   1000000000000000005LL;
#define                    ALL(___vect)   ___vect.begin(), ___vect.end()
#define              LEN(___vecx, Type)   (Type) ___vecx.size()
#define                          un_map   unordered_map
#define                          un_set   unordered_set


template<typename T> void _scan(T &x) { 
    x = 0; bool neg = 0; 
    register T c = getchar();
    if (c == '-') neg = 1, c = getchar();
    while ((c < 48) || (c > 57)) c = getchar();
    for ( ; c < 48||c > 57 ; c = getchar());
    for ( ; c > 47 && c < 58; c = getchar() ) x= (x << 3) + ( x << 1 ) + ( c & 15 );
    if (neg) x *= -1;
}


void printYesNo(bool Expr, int YNType = 1, string FirstChoice = "Ud", string SecondChoice = "Ud") { 
    if (YNType == 1) puts(Expr ? "YES" : "NO");
    else if (YNType == 2) puts(Expr ? "Yes" : "No");
    else if (YNType == 3) puts(Expr ? "yes" : "no");
    else if (YNType == 4) cout << (Expr ? FirstChoice : SecondChoice);
}


void solveEach() {
    lld n, k;
    cin >> n >> k;
    STR s; cin >> s;
    bool allowedLetters[26] = {false};
    FORFWD(i, 0, k, 1) {
        char temp; cin >> temp;
        allowedLetters[temp-'a'] = true;
    }

    lld ans = 0;
    FORFWD(i, 0, n, 1) {
        lld j = i;
        while (allowedLetters[s[j]-'a'] and j < n) j++;
        ans += ((j-i+1) * (j-i))/2;
        i = j;
    }

    cout << ans << "\n";

    return;
}


signed main() {

    // GREED_FOR_SPEED;

    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif 

    // TESTCASES_ARE_THERE()
        solveEach();
    return 0;
}

/*
THE LOGIC AND APPROACH IS MINE ( UDIT GUPTA )
SOME PARTS OF THE CODE MAY HAVE BEEN TAKEN FROM WEBSITES LIKE::
(I Own the code if no link is provided here or I may have missed mentioning it)ch|=spacelo &=_up change case
*/