# Generated by Django 5.0.1 on 2024-01-15 21:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("TODO_list", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["-is_completed"]},
        ),
        migrations.AlterField(
            model_name="task",
            name="is_completed",
            field=models.BooleanField(default=False),
        ),
    ]
