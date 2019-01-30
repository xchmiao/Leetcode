DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        if board is None or len(board) == 0:
            return []
            
        word_set = set(words)
        prefix_set = set()
        # print(word_set)
        for word in words:
            for i in range(1, len(word) + 1):
                prefix_set.add(word[:i]) # add all prefix to prefix_set
        
        # print(sorted(list(prefix_set)))
                
        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.search(board, i, j, board[i][j],
                            word_set, prefix_set, set([(i, j)]), result)
                            
        return list(result)
        
        
    
    def search(self, board, x, y, word, word_set, prefix_set, visited, result):
        if word not in prefix_set:
            return
        
        if word in word_set:
            result.add(word)
            
        for delta_x, delta_y in DIRECTIONS:
            x_, y_ = x + delta_x, y + delta_y
            
            if not self.inside(board, x_, y_):
                continue
            
            if (x_, y_) in visited: # make sure for search each path, the (x, y) is not repeated
                continue
            
            visited.add((x_, y_))
            
            self.search(board, x_, y_, word + board[x_][y_], word_set,
                        prefix_set, visited, result)
                        
            visited.remove((x_, y_))
            
    def inside(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])
        
