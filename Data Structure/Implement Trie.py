"""
https://leetcode.com/problems/implement-trie-prefix-tree/
"""
class TrieNode:
    def __init__(self):
        self.children = {} # mapping char to TrieNode, i.e. char: TrieNode()
        self.is_word = False
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    def find(self, word: str) -> TrieNode:
        node = self.root
        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        
        node = self.root
        for c in word:
            # if c is not a child of current node, then create a new TrieNode for c
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        # at the end, set the is_word = True, i.e. flag it is word
        node.is_word = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        
        node = self.find(word)
        return node is not None and node.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.find(prefix)
        return node is not None
