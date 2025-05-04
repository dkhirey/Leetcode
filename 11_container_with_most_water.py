# leetcode 11_container_with_most_water.py
# https://leetcode.com/problems/container-with-most-water/
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
# which together with the x-axis forms a container, such that the container contains the most water.
# Note: You may not slant the container.    
# The container is formed by two lines and the x-axis. The area of the container is the minimum of the two heights
# multiplied by the distance between the two lines. The area is given by:
# area = min(height[i], height[j]) * (j - i)
# The maximum area is the maximum of all possible areas. The brute force solution is to check all pairs of lines,
# which takes O(n^2) time. We can do better by using a two-pointer approach, which takes O(n) time. 
# We start with two pointers, one at the beginning and one at the end of the array. We calculate the area formed by
# the two lines at the pointers and move the pointer that points to the shorter line towards the other pointer.
# This is because the area is limited by the shorter line, so moving the longer line will not increase the area.
# The two-pointer approach is more efficient because it reduces the number of pairs we need to check.
# The time complexity is O(n) and the space complexity is O(1).
# The two-pointer approach is a common technique used in many problems, including this one.

# class solution():	
#     def area(i,j,arr):
#         area = min(arr[i],arr[j])* (j-i)
#         return area
		
#     def main(arr):
#         b = 0
#         e = len(arr)-1
#         a = 1
		
#         for i in range(len(arr)):
#             if arr[b] >= arr[e]:
#                 # b = i
#                 e -= 1
#             else :
#                 b += 1
#                 # e = i
#             a = max(solution.area(b,e,arr),a)
#         print(a)
#         return a
	

#whats wrong with the code?
#The code is not returning the correct maximum area. The two-pointer approach is not implemented correctly.
#The pointers are not moving correctly, and the area is not being calculated correctly. 
#The area is being calculated correctly, but the pointers are not being moved correctly.
#The pointers should be moved based on the height of the lines, not the index.
#The two-pointer approach should be implemented as follows:
#1. Initialize two pointers, one at the beginning and one at the end of the array.
#2. Calculate the area formed by the two lines at the pointers. 
#3. Move the pointer that points to the shorter line towards the other pointer.
#4. Repeat steps 2 and 3 until the two pointers meet.
#5. Return the maximum area found.
#The time complexity is O(n) and the space complexity is O(1).      
#The two-pointer approach is a common technique used in many problems, including this one.
#working solution
class solution():	
    def area(i,j,arr):
        area = min(arr[i],arr[j])* (j-i)
        return area
        
    def main(arr):
        b = 0
        e = len(arr)-1
        a = 0
        
        while b < e:
            a = max(solution.area(b,e,arr),a)
            if arr[b] >= arr[e]:
                e -= 1
            else :
                b += 1
            print(b,e)
            print(a)
            
        return a
    
arr = [4,3,2,1,4] #[1,8,2,4,4,7,8,3]
solution.main(arr) 