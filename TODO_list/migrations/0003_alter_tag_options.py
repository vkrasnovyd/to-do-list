# Generated by Django 5.0.1 on 2024-01-15 21:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("TODO_list", "0002_alter_task_options_alter_task_is_completed"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tag",
            options={"ordering": ["name"]},
        ),
    ]