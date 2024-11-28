import unittest

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



class TestTree(unittest.TestCase):
    def setUp(self):
        """Tworzy przykładowe drzewo do testowania."""
        self.tree = Tree("Root")
        self.child_a = TreeNode("A")
        self.child_b = TreeNode("B")
        self.child_c = TreeNode("C")
        self.grandchild_a1 = TreeNode("A1")
        self.grandchild_a2 = TreeNode("A2")
        
        # Budowanie drzewa
        self.tree.root.add_child("edge1", self.child_a)
        self.tree.root.add_child("edge2", self.child_b)
        self.child_a.add_child("edge3", self.child_c)
        self.child_a.add_child("edge4", self.grandchild_a1)
        self.child_b.add_child("edge5", self.grandchild_a2)

    def test_tree_structure(self):
        """Testuje strukturę drzewa."""
        self.assertEqual(self.tree.root.value, "Root")
        self.assertIn("edge1", self.tree.root.children)
        self.assertIn("edge2", self.tree.root.children)
        self.assertEqual(self.tree.root.children["edge1"].value, "A")
        self.assertEqual(self.tree.root.children["edge2"].value, "B")

    def test_add_child(self):
        """Testuje dodawanie dzieci do węzła."""
        new_child = TreeNode("D")
        self.tree.root.add_child("edge6", new_child)
        self.assertIn("edge6", self.tree.root.children)
        self.assertEqual(self.tree.root.children["edge6"].value, "D")

    def test_traverse(self):
        """Testuje przechodzenie drzewa."""
        expected_traversal = ["Root", "A", "C", "A1", "B", "A2"]
        self.assertEqual(self.tree.traverse(), expected_traversal)

    def test_str_representation(self):
        """Testuje reprezentację drzewa w postaci string."""
        representation = str(self.tree)
        self.assertIn("Root", representation)
        self.assertIn("[edge1] -> A", representation)
        self.assertIn("[edge5] -> A2", representation)


if __name__ == "__main__":
    unittest.main()
