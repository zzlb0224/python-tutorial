# Generated by Django 2.2.7 on 2019-12-06 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fk', '0005_article_content3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='content3',
        ),
    ]
