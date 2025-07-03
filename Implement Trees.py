class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    
    def print_tree(self):
        print(self.data)
        if (self.children):
            for child in self.children:
                child.print_tree()
    
    def get_level(self):
        level=0
        node= self
        while node.parent:
            level+=1
            node=node.parent
        return level


def build_product_tree():
    root= TreeNode("Electronics")
    laptop= TreeNode("Laptop")
    desktop=TreeNode("Desktop")
    macbook=TreeNode("Macbook")

    root.add_child(laptop)
    root.add_child(desktop)

    laptop.add_child(macbook)

    print(macbook.get_level())

    return root


if __name__== "__main__":
    root=build_product_tree()
    root.print_tree()
    print(root.get_level())


