class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.children = {}  # Dzieci węzła w postaci {krawędź: TreeNode}

    def add_child(self, edge_label, child_node):
        """Dodaje dziecko do węzła z oznaczeniem krawędzi."""
        self.children[edge_label] = child_node

    def __str__(self, level=0, edge_label=None):
        """Rekurencyjnie tworzy reprezentację drzewa w postaci czytelnej."""
        prefix = " " * (level * 2) + (f"[{edge_label}] -> " if edge_label else "")
        result = f"{prefix}{self.value}\n"
        for edge, child in self.children.items():
            result += child.__str__(level + 1, edge)
        return result


class Tree:
    def __init__(self, root_value=None):
        self.root = TreeNode(root_value)

    def traverse(self):
        """Przechodzi wszystkie węzły drzewa w porządku DFS."""
        result = []

        def dfs(node):
            if node:
                result.append(node.value)
                for child in node.children.values():
                    dfs(child)

        dfs(self.root)
        return result

    def __str__(self):
        """Reprezentacja drzewa zaczynająca od korzenia."""
        return str(self.root)


# Przykład użycia
if __name__ == "__main__":
    # Tworzenie drzewa
    tree = Tree("Root")
    child_a = TreeNode("A")
    child_b = TreeNode("B")
    child_c = TreeNode("C")
    grandchild_a1 = TreeNode("A1")
    grandchild_a2 = TreeNode("A2")

    # Budowanie struktury drzewa
    tree.root.add_child("edge1", child_a)
    tree.root.add_child("edge2", child_b)
    child_a.add_child("edge3", child_c)
    child_a.add_child("edge4", grandchild_a1)
    child_b.add_child("edge5", grandchild_a2)

    # Wyświetlenie drzewa
    print("Drzewo:")
    print(tree)

    # Przejście drzewa i wyświetlenie wartości węzłów
    print("Przechodzenie drzewa:")
    print(tree.traverse())
