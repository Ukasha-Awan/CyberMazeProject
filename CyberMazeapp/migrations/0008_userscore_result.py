# Generated by Django 5.0.1 on 2025-01-17 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CyberMazeapp", "0007_alter_userscore_score"),
    ]

    operations = [
        migrations.AddField(
            model_name="userscore",
            name="result",
            field=models.CharField(
                choices=[("pass", "Pass"), ("fail", "Fail")],
                default="fail",
                max_length=10,
            ),
        ),
    ]
