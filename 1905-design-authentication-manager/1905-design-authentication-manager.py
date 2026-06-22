class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.token = {}
        self.ttl = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.token:
            return
        elif self.token[tokenId] <= currentTime:
            del self.token[tokenId]
        else:
            self.token[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        res = 0
        for tokenId, expiry in list(self.token.items()):
            if expiry <= currentTime:
                del self.token[tokenId]
            else:
                res += 1
        
        return res
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)