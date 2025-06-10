class Twitter:

    def __init__(self):
        self.time = 0
        self.user_tweets = defaultdict(list)
        self.user_follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        if userId in self.user_tweets:
           heap.extend(self.user_tweets[userId][-10:])
        if userId in self.user_follows:
            for followeeId in self.user_follows[userId]:
                if followeeId in self.user_tweets:
                    heap.extend(self.user_tweets[followeeId][-10:])

        heapq.heapify(heap)
        feed = []
        while heap and len(feed) < 10:
            feed.append(heapq.heappop(heap)[1])
        return feed
        
    def follow(self, followerId: int, followeeId: int) -> None:
        followers = self.user_follows[followerId]
        followers.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followers = self.user_follows[followerId]
        if followeeId in followers:
            followers.remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)