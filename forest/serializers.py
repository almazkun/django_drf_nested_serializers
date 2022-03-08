from rest_framework import serializers

from .models import Branch, Caterpillar, Forest, Leaf, Tree


class ForestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forest
        fields = "__all__"


class TreeSerializer(serializers.ModelSerializer):
    forest = ForestSerializer()

    class Meta:
        model = Tree
        fields = "__all__"

    def create(self, validated_data):
        forest_data = validated_data.pop("forest")
        forest = ForestSerializer(data=forest_data).create(forest_data)
        tree = Tree.objects.create(forest=forest, **validated_data)
        return tree


class BranchSerializer(serializers.ModelSerializer):
    tree = TreeSerializer()

    class Meta:
        model = Branch
        fields = "__all__"

    def create(self, validated_data):
        tree_data = validated_data.pop("tree")
        tree = TreeSerializer(data=tree_data).create(tree_data)
        branch = Branch.objects.create(tree=tree, **validated_data)
        return branch


class LeafSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()

    class Meta:
        model = Leaf
        fields = "__all__"

    def create(self, validated_data):
        branch_data = validated_data.pop("branch")
        branch = BranchSerializer(data=branch_data).create(branch_data)
        leaf = Leaf.objects.create(branch=branch, **validated_data)
        return leaf


class CaterpillarSerializer(serializers.ModelSerializer):
    leaf = LeafSerializer()

    class Meta:
        model = Caterpillar
        fields = "__all__"

    def create(self, validated_data):
        leaf_data = validated_data.pop("leaf")
        leaf = LeafSerializer(data=leaf_data).create(leaf_data)
        caterpillar = Caterpillar.objects.create(leaf=leaf, **validated_data)
        return caterpillar
