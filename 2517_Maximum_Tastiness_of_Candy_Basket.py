# 2517_Maximum_Tastiness_of_Candy_Basket.py
# leetcode 2517
# https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

# 2517. Maximum Tastiness of Candy Basket
# solution
# You are given an integer array price of length n, where price[i] is the price of the ith candy.
# You are also given an integer k, which represents the number of candies you can buy.
# You want to buy k candies such that the minimum tastiness of the candies is maximized.
# The tastiness of a candy is defined as the difference between the maximum and minimum prices of the candies you buy.
# You can buy the candies in any order.
# Return the maximum tastiness of the candies you can buy.
# Constraints:  
# 1 <= price.length <= 10^5
# 1 <= price[i] <= 10^9
# 1 <= k <= price.length
# The answer will be in the range [0, 10^9].

# Approach
# 1. Sort the price array in ascending order.   
# 2. Initialize two pointers, left and right, to the first and last elements of the sorted array, respectively.
# 3. Initialize a variable max_tastiness to 0.
# 4. While left < right:
#    a. Calculate the mid-point of the left and right pointers. 
#    b. Calculate the number of candies that can be bought with the current mid-point.
#    c. If the number of candies is greater than or equal to k, update max_tastiness to the maximum of max_tastiness and mid-point.
#    d. If the number of candies is less than k, move the left pointer to mid + 1.
#    e. If the number of candies is greater than or equal to k, move the right pointer to mid.
# 5. Return max_tastiness.

from typing import List
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        left, right = 0, price[-1] - price[0]
        max_tastiness = 0

        while left <= right:
            mid = (left + right) // 2
            count = 1
            last_price = price[0]

            for i in range(1, len(price)):
                if price[i] - last_price >= mid:
                    count += 1
                    last_price = price[i]

            if count >= k:
                max_tastiness = mid
                left = mid + 1
            else:
                right = mid - 1

        return max_tastiness
    
# time complexity: O(n log n)
# space complexity: O(1)
# where n is the length of the price array.
# The sorting step takes O(n log n) time, and the two-pointer traversal takes O(n) time.
# The overall time complexity is O(n log n).

