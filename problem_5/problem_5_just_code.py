class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        suffixes = []
        
        def suffix_helper(node, s):
            if node.is_word:
                suffixes.append(s)
                
            if not node.children:
                return 
        
            for char in node.children:
                suffix_helper(node.children[char], s + char)
            
        suffix_helper(self, suffix)
      
        return suffixes

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        for char in word:
            if char not in node.children:
                node.insert(char)
            node = node.children[char]
        node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node

test_trie_1 = Trie()
test_trie_1.insert("fun")
test_trie_1.insert("function")
test_trie_1.insert("factory")
test_trie_1.insert("gangster")
test_trie_1.insert("super")
test_trie_1.insert("supercalifragilisticexpialidocious")

#Test Case 1
test_node_1 = test_trie_1.find("f")
# print(test_node_1.suffixes())
#expected: ['un', 'unction', 'actory']

#Test Case 2
test_node_2 = test_trie_1.find("fu")
#print(test_node_2.suffixes())
#expected: ['n', 'nction']

#Test Case 3
test_node_3 = test_trie_1.find("fa")
# print(test_node_3.suffixes())
#expected: ['ctory']

#Test Case 4
test_node_4 = test_trie_1.find("gang")
#print(test_node_4.suffixes())
#expected: ['ster']

#Test Case 5
test_node_5 = test_trie_1.find("supercalifragilisticexpialidociou")
# print(test_node_5.suffixes())
#expected: ['s']

#Test Case 6
test_node_6 = test_trie_1.find("s")
#print(test_node_6.suffixes())
#expected: ['uper', 'upercalifragilisticexpialidocious']