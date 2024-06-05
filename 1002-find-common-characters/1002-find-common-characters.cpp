class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
    vector<int> common(26,INT_MAX);
    vector<string> d;

    for (auto m : words){
        vector<int> cnt(26, 0);
        for (auto c : m)
            cnt[c - 'a']++;
        for (auto i = 0; i < 26; i++)
            common[i] = min(common[i], cnt[i]);
    }

    for (auto i = 0; i < 26; i++)
        for (auto j = 0; j < common[i]; j++)
            d.push_back(string(1, i + 'a'));
        
    return d;
}
};

   