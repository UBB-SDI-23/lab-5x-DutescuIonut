# Generated by Django 4.1.7 on 2023-03-15 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("A1HW", "0003_rename_carstunedby_cartunedby"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartunedby",
            name="DateTuned",
            field=models.CharField(default="as", max_length=200),
        ),
        migrations.AddField(
            model_name="cartunedby",
            name="TuningPrice",
            field=models.IntegerField(default=50),
        ),
    ]