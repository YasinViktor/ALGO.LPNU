class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def pre_order_traversal(root: BinaryTree):
    result = []
    if root:
        result.append(root.value)
        result += pre_order_traversal(root.left)
        result += pre_order_traversal(root.right)
    return result

def main():
    # Створення бінарного дерева
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    """root.left.right = BinaryTree(0)
    
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)"""

    # Виконання прямого обходу
    print(pre_order_traversal(root))  # Виведе: [1, 2, 5, 3, 6, 7]

if __name__ == "__main__":
    main()
