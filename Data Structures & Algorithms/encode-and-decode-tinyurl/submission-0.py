class Solution:
    def __init__(self):
        self.longToShort = {}
        self.shortToLong = {}
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        print(longUrl)
        if longUrl not in self.longToShort:
            self.longToShort[longUrl] = str(self.counter)
            self.shortToLong[str(self.counter)] = longUrl
            self.counter += 1
        
        return self.longToShort[longUrl]

    def decode(self, shortUrl: str) -> str:
        print(shortUrl)
        if shortUrl not in self.shortToLong:
            return ""

        return self.shortToLong[shortUrl]
