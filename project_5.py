"""
Building a Trie in Python
1. Finding a Prefix
2. Finding suffix which starts with prefix letter
3. Printing all suffix with prefix

Time complexity will be O(n *m ) where n is number of words and m is max number of letter in a word
"""
## Represents a single node in the Trie

class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def suffix_recursive(self, prefix):
        # this is recursive function
        results = []
        if self.is_word:
            results.append(prefix)
        for value, child in self.children.items():
            results.extend(child.suffix_recursive(prefix + value))
        return results

    def suffixes(self, prefix):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        # handling None Prefix
        if prefix is None:
            return
        if self is None:
            return
        sub_results = self.suffix_recursive(prefix)
        # print(r)
        suffix_out = []
        for item in sub_results:
            # Removing prefix letter from the sub_results
            suffix_out.append(item[len(prefix):])
        return suffix_out


## The Trie itself containing the root node and insert/find functions

class Trie:

    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie

        if word == None:
            return
        current_node = self.root

        for char in word:
            if char not in current_node.children.keys():
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_word = True

    def exists(self, word):
        # Detect a null input and return
        if word is None:
            return

        # Check if word exist in Trie
        current_node = self.root

        for char in word:
            if char not in current_node.children.keys():
                return False
            current_node = current_node.children[char]
        return current_node.is_word

    # @pysnooper.snoop()
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        if prefix is None:
            return

        current_node = self.root
        # print(current_node.children)
        for char in prefix:
            if char not in current_node.children.keys():
                return None
            current_node = current_node.children[char]

        return current_node


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
    print(prefixNode.suffixes('a'))

    # Test Case 1
    Case1Trie = Trie()
    wordList1 = [
        "he", "hell", "hello", "helmet",
        "sun", "sunny", "summer", "summation"
    ]
    for word in wordList1:
        Case1Trie.insert(word)

    prefixNode1 = Case1Trie.find('h')
    print('-' * 10, "Case 1 Output", '-' * 10)
    print(prefixNode1.suffixes('h'))

    # Test Case 2, Only single letter starting Trie
    Case2Trie = Trie()
    wordList2 = [
        "tea", "team", "temperature", "temper",
        "teapot", "teller", "telling", "teleportation"
    ]
    for word in wordList2:
        Case2Trie.insert(word)

    prefixNode2 = Case2Trie.find('t')
    print('-' * 10, "Case 2 Output", '-' * 10)
    print(prefixNode2.suffixes('t'))

    # Test Case 3, Searching for letter when None value is input
    Case3Trie = Trie()
    wordList3 = [
        "tea", "team", "temperature", "temper",
        "teapot", "teller", "telling", "teleportation"
    ]
    for word in wordList3:
        Case3Trie.insert(word)

    prefixNode3 = Case3Trie.find('o')
    print('-' * 10, "Case 3 Output", '-' * 10)
    if prefixNode3 is not None:
        print(prefixNode3.suffixes('o'))
    else:
        print("No Such Prefix exist in Trie")
