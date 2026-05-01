class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followees = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        users = self.followees[userId] | {userId}

        for user in users:
            if user not in self.tweets:
                continue

            for time, tweetId in self.tweets[user]:
                heapq.heappush(heap, (-time, tweetId))

        result = []
        while heap and len(result) < 10:
            time, tweetId = heapq.heappop(heap)
            result.append(tweetId)

        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)
        
