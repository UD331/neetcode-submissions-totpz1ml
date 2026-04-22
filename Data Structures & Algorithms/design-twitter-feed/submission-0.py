from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)      # userId -> [(time, tweetId)]
        self.following = defaultdict(set)    # userId -> {followeeId}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []
        res = []

        # include self + followees
        users = self.following[userId] | {userId}

        # push latest tweet of each user into heap
        for u in users:
            if self.tweets[u]:
                time, tweetId = self.tweets[u][-1]
                idx = len(self.tweets[u]) - 1
                heapq.heappush(heap, (-time, tweetId, u, idx))

        # extract top 10 tweets
        while heap and len(res) < 10:
            time, tweetId, u, idx = heapq.heappop(heap)
            res.append(tweetId)

            # push next older tweet from same user
            if idx > 0:
                next_time, next_tweet = self.tweets[u][idx - 1]
                heapq.heappush(heap, (-next_time, next_tweet, u, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)