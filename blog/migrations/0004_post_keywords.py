# Generated by Django 3.2.4 on 2022-12-08 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20221208_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='keywords',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
    ]