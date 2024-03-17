from collections import defaultdict
from collections import deque

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(lambda: [])
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        # find connected components of the graph
        components = []
        traversed = set()

        def find_component(node, component):
            if not node in traversed:
                component[node] = graph[node]
                traversed.add(node)
                for next_node in graph[node]:
                    find_component(next_node, component)

        for node in range(1, n+1):
            if not node in traversed:
                component = dict()
                find_component(node, component)
                components.append(component)

        # for each component check if it is bipartite 
        for component in components:
            traversed = set()
            coloring = {}
            initial_node = next(iter(component))
            coloring[initial_node] = 1
            queue = deque([initial_node])

            while queue:
                node = queue.popleft()
                for next_node in component[node]:
                    if (node, next_node) not in traversed:
                        if next_node not in coloring:
                            coloring[next_node] = -1*coloring[node]
                            queue.append(next_node) 
                        else:
                            if coloring[next_node] != -1*coloring[node]:
                                return -1
                        traversed.add((node, next_node))
                        traversed.add((next_node, node))

        # if all components are bipartite
        # then calculate diameter of graph
        component_dist = [] 
        for component in components:
            nodes = list(component.keys())
            node_dist = []

            for node in nodes:
                distance = {}
                distance[node] = 1
                queue = deque([(1, node)])
                d = 1
                while queue:
                    d, cur_node = queue.popleft()
                    for next_node in component[cur_node]:
                        if next_node not in distance:
                            distance[next_node] = d+1
                            queue.append((d+1, next_node))
                max_dist = max(list(distance.values()))
                node_dist.append(max_dist)
            component_dist.append(max(node_dist))

        return sum(component_dist) 
