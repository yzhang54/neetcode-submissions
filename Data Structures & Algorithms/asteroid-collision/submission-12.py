class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        for asteroid in asteroids:
            kill = False
            # print(stack)
            while stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] > abs(asteroid):
                    kill = True
                    break
                elif stack[-1] < abs(asteroid):
                    stack.pop()
                else:
                    kill = True
                    stack.pop()
                    break

            if kill == False:
                stack.append(asteroid)

        return stack





            
                    
