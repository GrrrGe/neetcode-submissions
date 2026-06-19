class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.tweets = defaultdict(list)
        # self.allTweets = []
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time+=1
        # self.allTweets.append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        # feed = []
        feedIds = []
        self.users[userId].add(userId)
        for id in self.users[userId]:
            for t in self.tweets[id]:
                feedIds.append(t)
        # heapq.heapify(feedIds)
        return [k[1] for k in heapq.nlargest(10,feedIds)]
                
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
        
