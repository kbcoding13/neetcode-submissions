class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        #find leader of a
        #find leader of b

        #if the leaders are 

        rows, cols = len(grid), len(grid[0]) 
        

        parent = [i for i in range(0, rows * cols )]
        size = [1] * (rows * cols)
        
        def find(x:int) -> int:
            current = x
            while (parent[current] != current):
                current = parent[current]
            return current

        def union(a:int, b:int) -> bool:
            
            parent_a = find(a)
            parent_b = find(b)

            if parent_a == parent_b:
                return False

            else:
                if size[parent_a] > size[parent_b]:
                    size[parent_a] += size[parent_b]
                    parent[parent_b] = parent_a
                else:
                    size[parent_b] += size[parent_a]
                    parent[parent_a] = parent_b

                return True
        
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    if c + 1 < cols and grid[r][c + 1] == "1":
                        res = union(r * cols + c, r * cols + c + 1)
                        if res:
                            islands -= 1
                    if r + 1 < rows and grid[r + 1][c] == "1":
                        res = union((r + 1) * cols + c, r * cols + c)
                        if res:
                            islands -= 1
        
        return islands
                        

        
