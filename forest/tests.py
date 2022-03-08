from random import choice

from django.test import TestCase

from forest.models import Branch, Caterpillar, Forest, Leaf, Tree
from forest.serializers import CaterpillarSerializer


# Create your tests here.
class TestModels(TestCase):
    def setUp(self):
        self.caterpillar_name_list = [
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

    def test_caterpillars(self):
        forest = Forest.objects.create(name=choice(self.forest_name_list))

        n = choice(range(1, 3))

        tree_list = []
        for i in range(n):
            tree_list.append(
                Tree.objects.create(genus=choice(self.tree_genus_list), forest=forest)
            )

        branch_list = []
        for tree in tree_list:
            for i in range(n):
                branch_list.append(
                    Branch.objects.create(type=choice(self.branch_type_list), tree=tree)
                )

        leaf_list = []
        for branch in branch_list:
            for i in range(n):
                leaf_list.append(
                    Leaf.objects.create(
                        color=choice(self.leaf_colors_list), branch=branch
                    )
                )

        caterpillar_list = []
        for leaf in leaf_list:
            for i in range(n):
                caterpillar_list.append(
                    Caterpillar.objects.create(
                        name=choice(self.caterpillar_name_list), leaf=leaf, age=i
                    )
                )

        for caterpillar in caterpillar_list:
            self.assertTrue(caterpillar.name in self.caterpillar_name_list)
            self.assertTrue(caterpillar.leaf.color in self.leaf_colors_list)
            self.assertTrue(caterpillar.leaf.branch.type in self.branch_type_list)
            self.assertTrue(caterpillar.leaf.branch.tree.genus in self.tree_genus_list)
            self.assertTrue(
                caterpillar.leaf.branch.tree.forest.name in self.forest_name_list
            )

    def test_serializer_from_data(self):
        # fmt: off
        json = [
            {"id": 1, "leaf": {"id": 1, "branch": {"id": 1, "tree": {"id": 1, "forest": {"id": 1, "name": "Random"}, "genus": "Quercus"}, "type": "twigs"}, "color": "grey"}, "name": "Citheronia regalis", "age": 0},
            {"id": 2, "leaf": {"id": 1, "branch": {"id": 1, "tree": {"id": 1, "forest": {"id": 1, "name": "Random"}, "genus": "Quercus"}, "type": "twigs"}, "color": "grey"}, "name": "Garden tiger moth", "age": 0},
            {"id": 3, "leaf": {"id": 2, "branch": {"id": 1, "tree": {"id": 1, "forest": {"id": 1, "name": "Random"}, "genus": "Quercus"}, "type": "twigs"}, "color": "white"}, "name": "Citheronia regalis", "age": 0},
            {"id": 4, "leaf": {"id": 2, "branch": {"id": 1, "tree": {"id": 1, "forest": {"id": 1, "name": "Random"}, "genus": "Quercus"}, "type": "twigs"}, "color": "white"}, "name": "Citheronia regalis", "age": 0},
            {"id": 5, "leaf": {"id": 3, "branch": {"id": 2, "tree": {"id": 1, "forest": {"id": 1, "name": "Random"}, "genus": "Quercus"}, "type": "boughs"}, "color": "orange"}, "name": "Garden tiger moth", "age": 0},
            {"id": 6, "leaf": {"id": 3, "branch": {"id": 2, "tree": {"id": 1, "forest": {"id": 1, "name": "Random"}, "genus": "Quercus"}, "type": "boughs"}, "color": "orange"}, "name": "Peacock butterfly", "age": 0},
            {"id": 7, "leaf": {"id": 4, "branch": {"id": 2, "tree": {"id": 1, "forest": {"id": 1, "name": "Random"}, "genus": "Quercus"}, "type": "boughs"}, "color": "brown"}, "name": "Elephant hawk-moth", "age": 0},
            {"id": 8, "leaf": {"id": 4, "branch": {"id": 2, "tree": {"id": 1, "forest": {"id": 1, "name": "Random"}, "genus": "Quercus"}, "type": "boughs"}, "color": "brown"}, "name": "Citheronia regalis", "age": 0},
            {"id": 9, "leaf": {"id": 5, "branch": {"id": 3, "tree": {"id": 2, "forest": {"id": 1, "name": "Random"}, "genus": "Acer"}, "type": "boughs"}, "color": "black"}, "name": "Emperor moth ", "age": 0},
            {"id": 10, "leaf": {"id": 5, "branch": {"id": 3, "tree": {"id": 2, "forest": {"id": 1, "name": "Random"}, "genus": "Acer"}, "type": "boughs"}, "color": "black"}, "name": "Citheronia regalis", "age": 0},
            {"id": 11, "leaf": {"id": 6, "branch": {"id": 3, "tree": {"id": 2, "forest": {"id": 1, "name": "Random"}, "genus": "Acer"}, "type": "boughs"}, "color": "green"}, "name": "Elephant hawk-moth", "age": 0},
            {"id": 12, "leaf": {"id": 6, "branch": {"id": 3, "tree": {"id": 2, "forest": {"id": 1, "name": "Random"}, "genus": "Acer"}, "type": "boughs"}, "color": "green"}, "name": "Elephant hawk-moth", "age": 0},
            {"id": 13, "leaf": {"id": 7, "branch": {"id": 4, "tree": {"id": 2, "forest": {"id": 1, "name": "Random"}, "genus": "Acer"}, "type": "boughs"}, "color": "silver"}, "name": "Peacock butterfly", "age": 0},
            {"id": 14, "leaf": {"id": 7, "branch": {"id": 4, "tree": {"id": 2, "forest": {"id": 1, "name": "Random"}, "genus": "Acer"}, "type": "boughs"}, "color": "silver"}, "name": "Citheronia regalis", "age": 0},
            {"id": 15, "leaf": {"id": 8, "branch": {"id": 4, "tree": {"id": 2, "forest": {"id": 1, "name": "Random"}, "genus": "Acer"}, "type": "boughs"}, "color": "purple"}, "name": "Peacock butterfly", "age": 0},
            {"id": 16, "leaf": {"id": 8, "branch": {"id": 4, "tree": {"id": 2, "forest": {"id": 1, "name": "Random"}, "genus": "Acer"}, "type": "boughs"}, "color": "purple"}, "name": "Elephant hawk-moth", "age": 0},
        ]
        # fmt: on
        for caterpillar in json:
            cat = CaterpillarSerializer(data=caterpillar)

            cat.is_valid()
            cat.save()

            self.assertTrue(Caterpillar.objects.filter(id=cat.data["id"]).exists())
