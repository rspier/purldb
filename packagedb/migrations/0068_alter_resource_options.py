# Generated by Django 4.1.2 on 2023-07-04 01:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("packagedb", "0067_alter_resource_md5_alter_resource_sha1_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="resource",
            options={"ordering": ("id",)},
        ),
    ]
