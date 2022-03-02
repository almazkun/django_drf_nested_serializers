from django.test import TestCase
from forest.models import Forest, Tree, Branch, Leaf, Caterpillar
from random import choice
from forest.serializers import ForestSerializer


# Create your tests here.
class TestModels(TestCase):
    def setUp(self):
        self.catterpillar_name_list = [
            "Citheronia regalis",
            "Garden tiger moth",
            "Elephant hawk-moth",
            "Peacock butterfly",
            "Emperor moth ",
        ]

        self.leaf_colors_list = [
            "red",
            "green",
            "blue",
            "yellow",
            "orange",
            "purple",
            "pink",
            "brown",
            "black",
            "white",
            "grey",
            "silver",
            "gold",
        ]
        self.branch_type_list = ["boughs", "twigs"]
        self.tree_genus_list = [
            "Quercus",
            "Pinus",
            "Acer",
        ]

        self.forest_name_list = [
            "Random",
        ]

    def test_catterpillar(self):
        forest = Forest.objects.create(name=choice(self.forest_name_list))

        tree_list = []
        n = choice(range(1, 5))
        for i in range(n):
            tree_list.append(
                Tree.objects.create(genus=choice(self.tree_genus_list), forest=forest)
            )

        branch_list = []
        n = choice(range(1, 5))
        for tree in tree_list:
            for i in range(n):
                branch_list.append(
                    Branch.objects.create(type=choice(self.branch_type_list), tree=tree)
                )

        leaf_list = []
        n = choice(range(1, 5))
        for branch in branch_list:
            for i in range(n):
                leaf_list.append(
                    Leaf.objects.create(
                        color=choice(self.leaf_colors_list), branch=branch
                    )
                )

        catterpillar_list = []
        n = choice(range(1, 5))
        for leaf in leaf_list:
            for i in range(n):
                catterpillar_list.append(
                    Caterpillar.objects.create(
                        name=choice(self.catterpillar_name_list), leaf=leaf
                    )
                )

        forest = Forest.objects.get(name=forest.name)

        print(ForestSerializer(forest).data)
