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

        feed.sort(key=lambda x: -x[0])
        return [tId for _, tId in feed[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
