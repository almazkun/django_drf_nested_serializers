from rest_framework import serializers
from .models import Forest, Tree, Branch, Leaf, Caterpillar


class ForestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forest
        fields = "__all__"


class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = "__all__"


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"


class LeafSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaf
        fields = "__all__"


class CatterpillarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caterpillar
        fields = "__all__"
