class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        # for each wordQuiery[i] find a string from wordContainer that has longest common suffix with wordsQuery[i]
        # if there is a tie, find string smallest in length
        # return array of intergers ans, where ans[i] is the index of the string in 
        # wordsContainer that has the longest common suffix with wordsQuery[i]

        # len(wordsContainer) = n, len(wordsQuery) = m
        # if we try suffixes set, O(mw) time and space
        # then iterate wordsContainer, over wordsQuery = O(mnw) time

        # trie -> O(mw) time and O(26 * w) = O(w) space
        # then iterate wordsContainer over the trie -> O(nw) time

        # trie is better
        # we should have to store the word's index in wordsQuery along with each node, so we have O(1) access
        # how to handle tie breakers? collection of indexes and compare lengths that that point -> O(1), kind of messy though
        # or we can try to handle the tie breaker at the point of building the trie -> makes it easier for the "query" step since
        # there will only be one 
        
        # build the trie
        trie = {'': [{}, 0]}
        for i, word in enumerate(wordsContainer):
            root_i = trie[''][1]
            if len(wordsContainer[i]) < len(wordsContainer[root_i]):
                trie[''][1] = i
            curr = trie
            for ch in reversed(word): # go in reverse, building trie of suffixes
                if ch not in curr:
                    curr[ch] = [{}, i]
                else:
                    _, prev_i = curr[ch]
                    # update index only if current word is smaller
                    # < also handles tie breaker for occurrence
                    if len(wordsContainer[i]) < len(wordsContainer[prev_i]):
                        curr[ch][1] = i
                curr, _ = curr[ch]
        
        ans = [trie[''][1]] * len(wordsQuery)
        for i, word in enumerate(wordsQuery):
            curr = trie
            for ch in reversed(word):
                if ch not in curr:
                    break
                nextt, j = curr[ch]
                curr = nextt
                ans[i] = j
        
        return ans