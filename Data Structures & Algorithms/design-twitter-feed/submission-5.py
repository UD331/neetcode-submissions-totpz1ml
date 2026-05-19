class Twitter:
    def __init__(self):
        self.count = 0
        self.users = defaultdict(set)
        self.tweets = defaultdict(list)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.count, tweetId))
        self.count+=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        news = []
        news.extend(self.tweets[userId])
        for fol in self.users[userId]:
            news.extend(self.tweets[fol])
        heapq.heapify(news)
        feed = []
        for _ in range(min(10, len(news))):
            _, tweetId = heapq.heappop(news)
            feed.append(tweetId)
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)

        