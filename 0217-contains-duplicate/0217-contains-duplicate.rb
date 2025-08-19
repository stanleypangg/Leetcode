# @param {Integer[]} nums
# @return {Boolean}
require 'set'

def contains_duplicate(nums)
    nums_set = Set.new

    nums.each do |num|
        if nums_set.include?(num)
            return true
        end
        nums_set << num
    end

    false
end