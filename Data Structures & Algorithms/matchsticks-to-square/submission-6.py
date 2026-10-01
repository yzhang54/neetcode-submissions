class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
# [1,4,3,2,2,4]
#         1, 3
#         visited = 1, 3
        correctSideLen = sum(matchsticks)//4 

        if sum(matchsticks) % 4 != 0:
            return False

        # print(correctSideLen)
        visited = set()
        def backtrack(start, curSide, sidesDone):
            if curSide == correctSideLen:
                curSide = 0
                sidesDone += 1
                start = 0 
            if sidesDone == 4:
                return True
            if curSide > correctSideLen:
                return False 
                

            for index in range(start, len(matchsticks)):
                if index not in visited:
                    visited.add(index)
                    if backtrack(index+1, curSide + matchsticks[index], sidesDone):
                        return True
                    visited.remove(index)

            return False
        
        return backtrack(0, 0, 0)


                