# Generated by Django 4.1.4 on 2022-12-11 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_blog_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="time",
            field=models.DateField(),
        ),
    ]
