"""
HTTPRouter using Trie
HTTP Router is to take a URL path like "/", "/about", or
 "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return.
(root, None) -> ("about", None) -> ("me", "About Me handler")

Time complexity O(n*m) where n is number of words and m is max word length
"""


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler)
        self.error = None  # Will be used to publish 404 error

    def insert(self, path_list, input_handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

        current_node = self.root
        for word in path_list:
            if word not in current_node.children:
                current_node.children[word] = RouteTrieNode(None)
            current_node = current_node.children[word]

        # Adding handler to last value if input_handler hold any value
        current_node.handler = input_handler

    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if len(path_list) == 0:
            return self.root.handler

        current_node = self.root
        # This will be to handle last backslash /
        out_handler = None

        for word in path_list:
            # Checks if last word is backslash, execute if accordingly for out_handler
            if word not in current_node.children.keys() and word != '/':
                return self.error
            elif word not in current_node.children.keys() and word == '/':
                return out_handler

            if word != '/':
                current_node = current_node.children[word]
                out_handler = current_node.handler

        # If there is None in output handler, posting error instead
        if out_handler is None:
            return self.error
        return out_handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, path, handler):
        self.children[path] = RouteTrieNode(handler)

    def __repr__(self):
        return str(self.children)


class Router:
    def __init__(self, handler, error):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(handler)
        self.route_trie.root.handler = handler
        self.route_trie.error = error

    def add_handler(self, path, inp_handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_word = self.split_path(path)
        self.route_trie.insert(path_word, inp_handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_word = self.split_path(path)
        return self.route_trie.find(path_word)

    def split_path(self, sub_path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if sub_path == '/':
            return []

        split_path = sub_path.split('/')
        split_path.remove('')
        # handling backslash by adding backslash in output path and then have conditional find on it
        if sub_path[-1] == '/' and len(sub_path) > 1:
            split_path.remove('')
            split_path.append('/')

        return split_path


if __name__ == '__main__':
    # # create the router and add a route
    ### Test 0 ###
    print('-' * 10, 'Case 0', '-' * 10)
    router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route
    #
    # # some lookups with the expected output
    print(router.lookup("/"))  # should print 'root handler'
    print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
    print(router.lookup("/home/about"))  # should print 'about handler'
    print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
    print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one


    # Test Case 1 #
    print('-'*10, 'Case 1', '-'*10)
    case_router_1 = Router("root handler", "404 Page not found")
    case_router_1.add_handler("/course/security-architect-nanodegree--nd992", 'Course on Security Architect')

    print(case_router_1.lookup("/"))
    print(case_router_1.lookup("/home"))
    print(case_router_1.lookup("/course/security-architect-nanodegree--nd992"))

    # Test Case 2 #
    print('-' * 10, 'Case 2', '-' * 10)
    case_router_2 = Router("root handler", "404 Page not found")
    case_router_2.add_handler("/home/pet/favorite", 'Favorite Pets Section')
    case_router_2.add_handler("/home/pet/favorite/private/health", 'Health records of Pets')

    print(case_router_2.lookup("/"))
    print(case_router_2.lookup("/home"))
    print(case_router_2.lookup("/home/pet/favorite"))
    print(case_router_2.lookup("/home/pet/favorite/"))
    print(case_router_2.lookup("/home/pet/favorite/private"))

    # Test Case 3 #
    print('-' * 10, 'Case 3', '-' * 10)
    case_router_3 = Router("Root handler", "404 Page not found")
    case_router_3.add_handler("/life", 'life is good')

    print(case_router_3.lookup("/"))
    print(case_router_3.lookup("/life"))
    print(case_router_3.lookup("/life//")) ## handling double backslash with error


