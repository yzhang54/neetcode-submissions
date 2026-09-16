class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        # 我觉得我们需要先去sort 因为这样 我们可以有当前最大跟最小的元素 当它们相加时 会最大可能的小于 limit
        # 如果 left == right?
        people.sort()
        print(people)

        left, right = 0, len(people)-1
        boats = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                boats += 1
                left += 1
                right -= 1
            else:
                right -= 1
                boats += 1

        return boats

            