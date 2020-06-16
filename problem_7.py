class RouteTrieNode:
    def __init__(self):
        self.children = {}
        self.handler = None

    def insert(self, path_part):
        if path_part not in self.children:
            self.children[path_part] = RouteTrieNode()
    
    def get_handler(self):
        return self.handler

    def set_handler(self, handler):
        self.handler = handler

class RouteTrie:
    def __init__(self, handler):
        self.root = RouteTrieNode()
        self.root.set_handler(handler)

    def insert(self, path, handler):
        node = self.root
        path_parts = path.split('/')
        for path_part in path_parts:
            if path_part:
                node.insert(path_part)
                node = node.children[path_part]
        node.set_handler(handler)

    def find(self, path):
        node = self.root
        path_parts = path.split('/')
        for path_part in path_parts:
            if path_part:
                if path_part in node.children:
                    node = node.children[path_part]
                else:
                    return None
        return node.get_handler()

class Router:
    def __init__(self, handler, not_found_handler):
        self.route_trie = RouteTrie(handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        self.route_trie.insert(path, handler)

    def lookup(self, path):
        return self.route_trie.find(path) or self.not_found_handler


router = Router("root handler", "not found handler") 
router.add_handler("/home/about", "about handler") 
router.add_handler("/home/about/me", "me handler") 
router.add_handler("/home/contact", "contact handler") 
router.add_handler("/shop/", "shop handler") 

#Test Case 1
print(router.lookup("/")) 
#expected: root handler

#Test Case 2
print(router.lookup("/home")) 
#expected: not found handler

#Test Case 3
print(router.lookup("/home/about")) 
#expected: about handler

#Test Case 4
print(router.lookup("/home/about/")) 
#expected: about handler

#Test Case 5
print(router.lookup("/home/about/me")) 
#expected: me handler

#Test Case 6
print(router.lookup("/home/contact"))
#expected: contact handler

#Test Case 7
print(router.lookup("shop"))
#expected: shop handler

#Test Case 7
print(router.lookup("home/contact/myspace"))
#expected: not found handler