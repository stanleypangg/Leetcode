# @param {String} s
# @param {String} t
# @return {Boolean}
def is_anagram(s, t)
    s_count = {}
    s.each_char do |c|
        s_count[c] = s_count.fetch(c, 0) + 1
    end
    
    t_count = {}
    t.each_char do |c|
        t_count[c] = t_count.fetch(c, 0) + 1
    end

    s_count == t_count
end