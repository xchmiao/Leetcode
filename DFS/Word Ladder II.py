## Problem: https://www.lintcode.com/problem/word-ladder-ii/description?_from=ladder&&fromId=1

from collections import deque

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        dict.add(start)
        dict.add(end)
        
        indexes = {}
        self.build_indexes(dict, indexes)
        
        # for end to start, find the distance from end to any given node
        distance = {}
        self.bfs(end, start, indexes, distance)
        
        # use DFS to search for all the paths from start to end
        results = []
        self.dfs(start, end, distance, indexes, [start], results)
        
        return results
        
    def build_indexes(self, dict, indexes):
        for word in dict:
            for i in range(len(word)):
                key = word[:i] + '%' + word[i+1:] # % is a matching character or index
                if key in indexes:
                    indexes[key].add(word)
                else:
                    indexes[key] = set([word])
        
    
    def get_next_words(self, word, indexes):
        words = []
        for i in range(len(word)):
            key = word[:i] + '%' + word[i+1:]
            for w in indexes.get(key, []):
                words.append(w)
        return words
        
        
    def bfs(self, start, end, indexes, distance):
        queue = deque([start])
        distance[start] = 0
        
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, indexes):
                if next_word not in distance: # make sure next_word has not been visited yet 
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)
                
    def dfs(self, curt, target, distance, indexes, path, results):
        if curt == target:
            results.append(list(path))
            
        for word in self.get_next_words(curt, indexes):
            if distance[word] != distance[curt] - 1: # make sure each time the distance is decrease by 1
                continue
            path.append(word)
            self.dfs(word, target, distance, indexes, path, results)
            path.pop()
