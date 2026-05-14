class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set) # k: userId v: followeeId
        self.tweetMap = defaultdict(list) # k: userId v: tweetId
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.tweetMap[userId][:]
        for user in self.followMap[userId]:
            feed.extend(self.tweetMap[user])

        feed = [(-t, tId) for t, tId in feed]
        heapq.heapify(feed)
        res = []
        for _ in range(min(10, len(feed))):
            res.append(heapq.heappop(feed)[1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
