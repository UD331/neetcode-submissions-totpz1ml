class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        # Step 2: Zero out rows
        for i in rows:
            matrix[i] = [0] * len(matrix[0])

        # Step 3: Zero out columns
        for j in cols:
            for i in range(len(matrix)):
                matrix[i][j] = 0

        