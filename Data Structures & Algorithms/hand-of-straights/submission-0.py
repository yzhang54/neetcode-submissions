class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        count = Counter(hand)
        hand.sort()

        for i in range(len(hand)):
            if count[hand[i]]:
                for j in range(hand[i], hand[i]+groupSize):
                    if not count[j]:
                        return False
                    count[j]-=1


        return True

