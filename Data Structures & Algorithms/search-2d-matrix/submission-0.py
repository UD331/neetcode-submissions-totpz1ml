class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if target <= matrix[i][n-1]:
                arr = matrix[i]
                l = 0
                r = n-1
                while (l<=r):
                    mid = int((l+r)/2)
                    if target < arr[mid]:
                        r = mid - 1
                    elif target > arr[mid]:
                        l = mid + 1
                    else:
                        return True

        return False