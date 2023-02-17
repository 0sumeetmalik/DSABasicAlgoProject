"""
Building a Trie in Python
1. Finding a Prefix
2. Finding suffix which starts with prefix letter
3. Printing all suffix with prefix
"""
import pysnooper


## Represents a single node in the Trie

class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix='', suffix_list =[]):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        if self.is_word:
            suffix_list.append(suffix)
            suffix = ''

        """
        Need Help here: I have tried a lot but when there are more than 1 item
        During Recursive call, last letter still remain in Suffix and prints out rest of letter with that extra letter
        I have tried various thing but not able to get my error, even though i have initiated suffix = ''
        
        """
        for letter in self.children:
            suffix += letter
            self.children[letter].suffixes(suffix)
        return suffix_list


## The Trie itself containing the root node and insert/find functions

class Trie:

    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie

        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_word = True

    # @pysnooper.snoop()
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        # print(current_node.children)
        while current_node is not None:
            # print('Scanning current node...', current_node.children)
            if prefix not in current_node.children:
                current_node = current_node.children
            else:
                return current_node.children[prefix]
        return None


if __name__ == '__main__':
    MyTrie = Trie()
    wordList = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]
    for word in wordList:
        MyTrie.insert(word)

    # Checking if nodes were created
    # print(MyTrie.root.children)
    prefixNode = MyTrie.find('a')
    print(prefixNode.suffixes())
