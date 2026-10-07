class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        Rqueue = deque()
        Dqueue = deque()

        for i in range(len(senate)):
            player = senate[i]
            if player == "R":
                Rqueue.append(i)
            else:
                Dqueue.append(i)

        # curPlayer = senate[0]
        while Rqueue and Dqueue:
            if Rqueue[0] < Dqueue[0]:
                Rqueue.append(Rqueue.popleft() + len(senate))
                Dqueue.popleft()
            else:
                Dqueue.append(Dqueue.popleft() + len(senate))
                Rqueue.popleft()
        
        return "Radiant" if Rqueue else "Dire"