# Generated by Django 5.0.6 on 2024-05-22 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quotes", "0002_rename_tags_quote__tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quote",
            name="_tags",
            field=models.TextField(db_column="tags"),
        ),
    ]
