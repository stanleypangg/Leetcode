# @param {String[]} strs
# @return {String[][]}
def group_anagrams(strs)
    # Iterate over every string
    hash = {}
    strs.each do |s|
        counter = {}
        s.each_char do |c|
            counter[c] = counter.fetch(c, 0) + 1
        end
        hash[counter] = hash.fetch(counter, []) << s
    end
    hash.values
end