"""
https://leetcode.com/problems/network-delay-time/

Solution: BFS + Heap

Note: 
1. using heap to garanutee that every loop, we viisted the nearest node first.
2. If the node has not been visited before, add the travel time to hash map (i.e. visited)
3. for the node's neighbor, if they also have not been visited before, put into the heap, in this way, we can make sure we 
only push the min_travel_time_to_node into the heap
"""

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
    
        from heapq import heapify, heappop, heappush
        
        graph = {node: set() for node in range(1, N + 1)}
        
        for node_out, node_in, time in times:
            graph[node_out].add((node_in, time))
        
        # start a heapq with tuples, tuple = (min_travel_time_to_node, node)
        queue = [(0, K)]
        heapify(queue)
        visited = {} # save the min travel time for every node in the dict
        
        while queue:
            time, node = heappop(queue)
            if node in visited:
                continue
            visited[node] = time
            for neighbor, add_time in graph[node]:
                if neighbor in visited:
                    continue
                heappush(queue, (time + add_time, neighbor))
                
        return max(visited.values()) if len(visited) == N else -1
