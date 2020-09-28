class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    
    [Description]:
    1. get stats on indegrees for all nodes
    2. put those nodes with indegree = 0 into queue
    3. while queue is not empty
        get an node from queue, and put the node in result, and reduce all its neighbor node's indegree by 1. If any neighbor node's indegree drops to zero, put it into the queue
    4. return result
    """
    def topSort(self, graph):
        # write your code here
        from collections import deque
        
        if not graph:
            return []
        
        indegree = self.get_indegree(graph)

        start_nodes = [x for x in graph if indegree[x] == 0]
        queue = deque(start_nodes)
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in node.neighbors:
                indegree[neighbor] -= 1 
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result
        
    
    def get_indegree(self, graph):
        # indegree = {x: 0 for x in graph}
        indegree = collections.defaultdict(int)
        for node in graph:
            for n in node.neighbors:
                indegree[n] += 1 
        
        return indegree
