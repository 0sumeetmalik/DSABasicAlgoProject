"""
HTTPRouter using Trie
HTTP Router is to take a URL path like "/", "/about", or
 "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return.
(root, None) -> ("about", None) -> ("me", "About Me handler")
"""

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()


    def insert(self, path):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        # path /home/about/me



    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

    def getNode(self):
        return RouteTrieNode()

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler


    def insert(self, sub_path):
        # Insert the node as before
        self.children[sub_path] = RouteTrieNode()
