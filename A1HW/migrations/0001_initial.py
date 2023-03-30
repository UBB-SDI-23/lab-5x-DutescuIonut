# Generated by Django 4.1.7 on 2023-03-15 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CarBrand",
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
                ("CarBrand", models.CharField(max_length=200)),
                ("Founded", models.CharField(max_length=200)),
                ("CEO", models.CharField(max_length=100)),
                ("NumberOfEmployees", models.IntegerField(default=1)),
                ("NetIncome", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Owner",
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
                ("LastName", models.CharField(max_length=100)),
                ("FirstName", models.CharField(max_length=100)),
                ("CNP", models.CharField(max_length=50)),
                ("Email", models.CharField(max_length=100)),
                ("Address", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Car",
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
                ("CarModel", models.CharField(max_length=200)),
                ("ProductionYear", models.IntegerField(default=0)),
                ("SeatsNumber", models.IntegerField(default=0)),
                ("Color", models.CharField(max_length=50)),
                (
                    "CarBrand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cars",
                        to="A1HW.carbrand",
                    ),
                ),
                (
                    "OwnerCNP",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cars",
                        to="A1HW.owner",
                    ),
                ),
            ],
        ),
    ]
