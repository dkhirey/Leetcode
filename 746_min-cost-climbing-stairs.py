# 746_min-cost-climbing-stairs.py
# https://leetcode.com/problems/min-cost-climbing-stairs/
# 1. If there is only one or two steps, the cost is the minimum of the two steps.
# 2. If there are more than two steps, the cost of the i-th step is the cost of the i-th step plus the minimum of the i-1-th step and the i-2-th step.
# 3. The minimum cost of the last two steps is the answer.
# Time complexity: O(n)
# Space complexity: O(n)

def minCostClimbingStairs(cost):
    n = len(cost)
    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    return min(dp[-1], dp[-2])

## Alternate solution traversing from the end
# Time complexity: O(n)
# Space complexity: O(1)**
def minCostClimbingStairs(cost):
    n = len(cost)
    # Traverse from the end and update the cost of each step with the minimum of the next two steps.
    for i in range(n-3, -1, -1):
        # Update the cost of the i-th step with the minimum of the i+1-th step and the i+2-th step.
        cost[i] += min(cost[i+1], cost[i+2])
    # The minimum cost of the first two steps is the answer
    return min(cost[0], cost[1])