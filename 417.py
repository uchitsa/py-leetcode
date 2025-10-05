class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        
        # Множества для хранения достижимых клеток
        pacific_reachable = set()
        atlantic_reachable = set()
        
        def dfs(r, c, reachable):
            """DFS для поиска достижимых клеток"""
            reachable.add((r, c))
            
            # Проверяем всех соседей
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                # Если сосед в пределах матрицы, еще не посещен,
                # и высота >= текущей (вода может течь ОТ океана ВВЕРХ)
                if (0 <= nr < rows and 0 <= nc < cols and 
                    (nr, nc) not in reachable and 
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, reachable)
        
        # Запускаем DFS от Тихого океана (левая и верхняя границы)
        for i in range(rows):
            dfs(i, 0, pacific_reachable)  # Левая граница
        for j in range(cols):
            dfs(0, j, pacific_reachable)  # Верхняя граница
        
        # Запускаем DFS от Атлантического океана (правая и нижняя границы)
        for i in range(rows):
            dfs(i, cols - 1, atlantic_reachable)  # Правая граница
        for j in range(cols):
            dfs(rows - 1, j, atlantic_reachable)  # Нижняя граница
        
        # Находим пересечение - клетки, достижимые из обоих океанов
        return list(pacific_reachable & atlantic_reachable)
