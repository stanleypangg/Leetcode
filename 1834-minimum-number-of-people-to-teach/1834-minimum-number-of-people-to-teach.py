class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        users_to_teach = set()
        
        for u, v in friendships:
            # shift zero-index
            u -= 1
            v -= 1

            can_communicate = False

            for u_lang in languages[u]:
                if u_lang in languages[v]:
                    can_communicate = True
                    break
                
            if not can_communicate:
                users_to_teach.add(u)
                users_to_teach.add(v)
        
        res = len(users_to_teach)
        for lang in range(1, n + 1):
            running_sum = 0
            
            for user in users_to_teach:
                if lang not in languages[user]:
                    running_sum += 1
                
            res = min(running_sum, res)

        return res