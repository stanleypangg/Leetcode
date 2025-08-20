class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> hashset;
        for (int num : nums) {
            if (hashset.contains(num)) return true;
            hashset.insert(num);
        }
        return false;
    }
};