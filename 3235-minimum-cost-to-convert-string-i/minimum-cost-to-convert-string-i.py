class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        INF = sys.maxsize
        graph = {chr(i): {chr(j): INF for j in range(ord('a'), ord('z') + 1)} for i in range(ord('a'), ord('z') + 1)}
        
        # Set the cost for each given conversion
        for o, c, z in zip(original, changed, cost):
            graph[o][c] = min(graph[o][c], z)
        
        # Set the cost of converting a character to itself to zero
        for char in graph:
            graph[char][char] = 0
        
        # Floyd-Warshall algorithm to find shortest path between all pairs of nodes
        for k in graph:
            for i in graph:
                for j in graph:
                    if graph[i][j] > graph[i][k] + graph[k][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]
        
        # Calculate the total minimum cost to convert source to target
        total_cost = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            if graph[s][t] == INF:
                return -1
            total_cost += graph[s][t]
        
        return total_cost

        