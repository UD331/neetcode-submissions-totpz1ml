class Twitter:
    def __init__(self):
        self.following = defaultdict(set)
        self.posts = defaultdict(list)
        self.t = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((-self.t, tweetId))
        self.t+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        self.follow(userId,userId)
        for following in self.following[userId]:
            for p in self.posts[following]:
                heapq.heappush(heap, p)

        res = []
        while heap and len(res) < 10:
            t, i = heapq.heappop(heap)
            res.append(i)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

        