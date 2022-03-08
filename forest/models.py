from django.db import models

_ = lambda s: s

# Create your models here.


class Forest(models.Model):
    name = models.CharField(_("Name"), max_length=255)

    def __str__(self):
        return f"Forest(name={self.name})"


class Tree(models.Model):
    genus = models.CharField(_("Genus"), max_length=255)
    forest = models.ForeignKey(_("Forest"), on_delete=models.CASCADE)

    def __str__(self):
        return f"Tree(genus={self.genus}, forest={self.forest})"


class Branch(models.Model):
    type = models.CharField(_("Type"), max_length=50)
    tree = models.ForeignKey(_("Tree"), on_delete=models.CASCADE)

    def __str__(self):
        return f"Branch(type={self.type}, tree={self.tree})"


class Leaf(models.Model):
    color = models.CharField(_("Color"), max_length=255)
    branch = models.ForeignKey(_("Branch"), on_delete=models.CASCADE)

    def __str__(self):
        return f"Leaf(color={self.color}, branch={self.branch})"


class Caterpillar(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    age = models.IntegerField(_("Age"), default=0)
    leaf = models.ForeignKey(_("Leaf"), on_delete=models.CASCADE)

    def __str__(self):
        return f"Caterpillar(name={self.name}, age={self.age}, leaf={self.leaf})"
