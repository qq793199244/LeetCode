'''
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，
其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
示例:
board =
 [['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']]
给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
'''
class Solution:
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(x, y, idx):
            if idx == len(word):
                return True
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or board[x][y] != word[idx]:
                return False
            visited[x][y] = 1
            for (i, j) in directions:
                if dfs(x+i, y+j, idx+1):
                    return True
            visited[x][y] = 0
            return False
        for x in range(m):
            for y in range(n):
                if dfs(x, y, 0):
                    return True
        return False


if __name__ == '__main__':
    u = Solution()
    board = [['A','B','C','E'],
             ['S','F','C','S'],
             ['A','D','E','E']]
    word1 = "ABCCED"
    word2 = "SEE"
    word3 = "ABCB"
    print(u.exist(board, word1))
    print(u.exist(board, word2))
    print(u.exist(board, word3))