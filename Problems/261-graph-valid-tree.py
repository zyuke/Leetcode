
from typing import (
    List,
)
from collections import defaultdict

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        graph = defaultdict(lambda: [])
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        visited = set()
        queue = [0]
        while queue:
            cur_node = queue.pop(0)
            visited.add(cur_node)
            for next_node in graph[cur_node]:
                if next_node not in visited:
                    queue.append(next_node)

        return len(visited) == n
