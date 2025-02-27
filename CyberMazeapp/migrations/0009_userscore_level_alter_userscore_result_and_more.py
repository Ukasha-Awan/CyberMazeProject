# Generated by Django 5.0.1 on 2025-01-18 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CyberMazeapp", "0008_userscore_result"),
    ]

    operations = [
        migrations.AddField(
            model_name="userscore",
            name="level",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="userscore",
            name="result",
            field=models.CharField(default="fail", max_length=10),
        ),
        migrations.AlterField(
            model_name="userscore",
            name="score",
            field=models.IntegerField(default=0),
        ),
    ]
