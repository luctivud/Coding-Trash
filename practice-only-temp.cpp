/*     <<<  J A I ~ S H R E E ~ R A M  >>>     */

// Title: practice-only-temp.cpp
// created on: 20-07-2020 at 18:20:23
// Creator & Template : Udit Gupta "@luctivud"
// https://github.com/luctivud
// https://www.linkedin.com/in/udit-gupta-1b7863135/


#include <bits/stdc++.h>
// #include <iostream>
// #include <string>
// #include <vector>
// #include <algorithm>
// #include <sstream>
// #include <queue>
// #include <deque>
// #include <bitset>
// #include <iterator>
// #include <list>
// #include <stack>
// #include <map>
// #include <set>
// #include <functional>
// #include <numeric>
// #include <utility>
// #include <limits>
// #include <time.h>
// #include <math.h>
// #include <stdio.h>
// #include <string.h>
// #include <stdlib.h>
// #include <assert.h>

using namespace std;

typedef long long int lld;
typedef unsigned long long int llu;
typedef vector<int> v_int;
typedef vector<lld> v_lld;
typedef vector<llu> v_llu;
typedef pair<int, int> p_int;
typedef pair<lld, lld> p_lld;


#define                   GREED_FOR_SPEED   ios_base::sync_with_stdio(false); cin.tie(0)
#define             TESTCASES_ARE_THERE()   cin >> (Test0xo); T35TC4535 = Test0xo; while(Test0xo--)
#define                  _INP14T(V3CT07)   for(auto &V3CT07_IT7T : (V3CT07)) cin >> (V3CT07_IT7T)
#define                 mems(A77AY, V4LU)   memset((A77AY), (V4LU), sizeof((A77AY)))
#define              CHECKC0N(IT7T, E9xD, St3P)    (((St3P)<0) ? (IT7T)>(E9xD) : (IT7T)<(E9xD))
#define  FOR4NGE(IT7T, ST47T, E9xD, St3P)   for(auto IT7T = (ST47T); CHECKC0N(IT7T, (E9xD), (St3P)); (IT7T) += (St3P))
#define            FORE4CH(IT7T, V3CT07)   for(auto IT7T = (V3CT07).begin(); IT7T != (V3CT07).end(); IT7T++)
#define           FORALL7(IT7T, V3CT07)   for (auto IT7T : (V3CT07))
#define                  ALL7L(V3CT07)   (V3CT07).begin(), (V3CT07).end()
#define                  RAL7L(V3CT07)   (V3CT07).rbegin(), (V3CT07).rend()
#define                              endl   "\n"
#define                            un_map   unordered_map
#define                            un_set   unordered_set


// template<typename T> void _SC4N(T &x) { 
//     x = 0; bool neg = 0; 
//     register T c = getchar();
//     if (c == '-') neg = 1, c = getchar();
//     while ((c < 48) || (c > 57)) c = getchar();
//     for ( ; c < 48||c > 57 ; c = getchar());
//     for ( ; c > 47 && c < 58; c = getchar() ) x= (x << 3) + ( x << 1 ) + ( c & 15 );
//     if (neg) x *= -1;
// }


// _PRi14T(arr);
template<typename Typ30f1> 
void _PRi14T(vector <Typ30f1> arr,  bool newline = false, string sep = " ") {
    for (auto item: arr) cout << item << sep;
    if (newline) cout << "\n";
}


void printYesNo(bool Expr, int YNType = 1, string FirstChoice = "Ud", string SecondChoice = "Ud") { 
    if (YNType == 1) puts(Expr ? "YES" : "NO");
    else if (YNType == 2) puts(Expr ? "Yes" : "No");
    else if (YNType == 3) puts(Expr ? "yes" : "no");
    else if (YNType == 4) cout << (Expr ? FirstChoice : SecondChoice);
}



void solveEach(lld T35TC453N = 1) {
    FOR4NGE(i, 1, 5, 1) cout << i;
    cout << "\n";
    FOR4NGE(i, 5, 1, -1) cout << i;

    cout << "\n"; 
    return;
}


signed main() {

    // GREED_FOR_SPEED;

    lld Test0xo = 0, T35TC4535 = 1;

    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif 

    // TESTCASES_ARE_THERE()
        solveEach(T35TC4535 - Test0xo);
    return 0;
}

/*
THE LOGIC AND APPROACH IS MINE ( UDIT GUPTA )
SOME PARTS OF THE CODE MAY HAVE BEEN TAKEN FROM WEBSITES LIKE::
(I Own the code if no link is provided here or I may have missed mentioning it)ch|=spacelo &=_up change case
*/