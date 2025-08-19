# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    hash = {}
    nums.each_with_index do |num, i|
        complement = target - num
        return [i, hash[complement]] if hash.key?(complement) && hash[complement] != i
        hash[num] = i
    end
end