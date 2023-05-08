from typing import List

"""
Solution:
    1. Provinces are assumed to be equal to number of cities.
    2. Main loop: Start point and start looping through cities.
    3. If the city we loop through is not visited it is one province.
    4. dfs method called for every city and its city that it is directly connected with.
"""


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = []
        provinces = 0

        def dfs(city):
            visited.append(city)
            for neighbor in range(n):
                if isConnected[city][neighbor] and neighbor not in visited:
                    dfs(neighbor)
        
        for city in range(n):
            if city not in visited:
                provinces += 1
                dfs(city)
                
        return provinces