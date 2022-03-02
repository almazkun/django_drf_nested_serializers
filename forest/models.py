from django.db import models

_ = lambda s: s

# Create your models here.
class Caterpillar(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    age = models.IntegerField(_("Age"), default=0)
    leaf = models.ForeignKey(_("Leaf"), on_delete=models.CASCADE)


class Leaf(models.Model):
    color = models.CharField(_("Color"), max_length=255)
    branch = models.ForeignKey(_("Branch"), on_delete=models.CASCADE)


class Branch(models.Model):
    type = models.CharField(_("Type"), max_length=50)
    tree = models.ForeignKey(_("Tree"), on_delete=models.CASCADE)

    def __repr__(self):
        return f"Branch: {self.type}, Tree: {self.tree}"


class Tree(models.Model):
    genus = models.CharField(_("Genus"), max_length=255)
    forest = models.ForeignKey(
        _("Forest"), on_delete=models.CASCADE, related_name="forest"
    )

    def __repr__(self):
        return f"Tree: {self.genus}, Forest: {self.forest}"


class Forest(models.Model):
    name = models.CharField(_("Name"), max_length=255)

    def __repr__(self):
        return f"Forest: {self.name}"
