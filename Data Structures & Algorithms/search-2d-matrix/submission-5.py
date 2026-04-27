class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        average = []
        for i in range(0, len(matrix)):
            temp = sum(matrix[i]) / len(matrix[i])
            average.append(temp)
        print(average)
        left, right = 0, len(matrix) - 1
        while right - left > 1:
            mid = (left + right) // 2
            if average[mid] < target:
                left = mid
            elif average[mid] > target:
                right = mid
            else:
                return True
        print(abs(average[left] - target))
        print(abs(average[right] - target))
        if matrix[left][-1] >= target:
            ans_1 = left
        else:
            ans_1 = right
        print(ans_1)
        
        left, right = 0, len(matrix[ans_1]) -1
        while left <= right:
            mid = (left + right) // 2
            
            if matrix[ans_1][mid] < target:
                left = mid + 1
            elif matrix[ans_1][mid] > target:
                right = mid - 1
            else:
                return True
        
        return False