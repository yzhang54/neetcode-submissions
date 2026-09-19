class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []
        for pos, spe in zip(position, speed):
            times.append([pos, spe])
        times.sort()
        stack = []
        for pos, spe in times:
            time = (target-pos)/spe

            while stack and stack[-1] <= time:
                tmp = stack.pop()

            stack.append(time)


        return len(stack)

        
        
