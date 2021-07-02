class Solution(object):
    def numIslands(self, grid):
        def dfs(i, j):
            # 육지가 아닐 경우 가지치기
            if i<0 or i>=len(grid) or \
                j<0 or j >=len(grid[0]) or \
                grid[i][j] != '1':
                    return
                
            t = 0
            u = 1
            grid[i][j] = "0"
        
            for k in range(4):  # 동서남북 탐색
                dfs(i+t, j+u)
                tmp = t
                t = -u
                u = tmp
                
        count = 0 # 섬의 개수
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count
        
