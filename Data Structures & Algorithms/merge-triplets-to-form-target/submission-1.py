class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        # bc if we apply max(), we would volate the rule
        # if we apply min(), we would 
        currentTriplet = [float("-inf"), float("-inf"), float("-inf")]
        for i in range(len(triplets)):
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                continue
            else:
                currentTriplet = [max(triplets[i][0], currentTriplet[0]), max(triplets[i][1], currentTriplet[1]), max(triplets[i][2], currentTriplet[2])]
            
            print(currentTriplet)

        return currentTriplet == target
