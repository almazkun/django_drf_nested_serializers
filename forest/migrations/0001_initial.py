# Generated by Django 4.0.2 on 2022-03-01 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Branch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.CharField(max_length=50, verbose_name="Type")),
            ],
        ),
        migrations.CreateModel(
            name="Forest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Name")),
            ],
        ),
        migrations.CreateModel(
            name="Tree",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("genus", models.CharField(max_length=255, verbose_name="Genus")),
                (
                    "forest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="forest.forest"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Leaf",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("color", models.CharField(max_length=255, verbose_name="Color")),
                (
                    "branch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="forest.branch"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Caterpillar",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                ("age", models.IntegerField(default=0, verbose_name="Age")),
                (
                    "leaf",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="forest.leaf"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="branch",
            name="tree",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="forest.tree"
            ),
        ),
    ]
