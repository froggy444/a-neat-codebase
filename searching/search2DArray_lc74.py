class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        row = len(matrix)
        col = len(matrix[0])
        
        right = (len(matrix) * len(matrix[0])) - 1
        mid = 0
        while left <= right: 
            mid = (left + right)// 2
            midElement = matrix[mid // col][mid % col]
            print(midElement)
            if  midElement == target :
                return True 
            elif midElement > target:  # explain formula 
                right = mid -1
            else:
                left = mid + 1
        
        return False