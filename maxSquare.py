class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        xlength = len(matrix[0])
        ylength = len(matrix)
        result = [([0]*xlength) for i in xrange(ylength)]

        for i in xrange(ylength):
            for j in xrange(xlength):
                if matrix[i][j] == 0:
                    continue

                if i == 0 or j == 0:
                    result[i][j] = matrix[i][j]
                else:
                    result[i][j] = min(result[i-1][j], result[i-1][j-1], result[i][j-1]) + matrix[i][j]

        print result

s = Solution()
matrix =[[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,1,1,1]]
s.maximalSquare(matrix)
