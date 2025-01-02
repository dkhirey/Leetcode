class Solution:
    def maxJump(self, stones: List[int]) -> int:
        cost = []
        start = 0
        while start <= len(stones)-1:
            visited = []
            jmax = 0
            reached = False
            prev = 0
            
            print("srtart...",start)
            print("forward pass....................... ")
            for idx,stone in enumerate(stones):
                if idx >= start:
                    visited.append(stone)
                    print(stone)
                    if (stone - prev) > jmax:
                        jmax = stone - prev
                        prev = stone
                        print("max jump forward...",jmax)
                    
            print("reverse pass....................... ")
            for stone in reversed(stones):
                if stone not in visited:
                    visited.append(stone)
                    print(stone)
                    if (prev - stone) > jmax:
                        jmax = prev - stone
                        prev = stone
                        print("max jump reverse...",jmax)
                    if stone == 0 :
                        reached = True
            if reached :
                cost.append(jmax)
                
            start += 1

        print(min(cost))
        return min(cost)

### basic solution for clear logic, not using DP       