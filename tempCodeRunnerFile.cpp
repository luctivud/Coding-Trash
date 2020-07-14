string s;
    vector<string> arr;
    while (cin >> s) arr.push_back(s);
    _C0UN73R <string , int> Obj(arr);
    map<string, int> count =  Obj.getCountAsMap();
    vector<pair<string, int>> sorted_count = Obj.getSortedVectorPair();
    FORA77L(so