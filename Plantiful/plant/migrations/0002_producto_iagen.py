# Generated by Django 4.2.dev20220603193729 on 2022-06-11 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("plant", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="producto",
            name="iagen",
            field=models.ImageField(null=True, upload_to="productos"),
        ),
    ]
