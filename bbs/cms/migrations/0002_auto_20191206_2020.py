# Generated by Django 2.2.7 on 2019-12-06 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0004_auto_20191206_2020'),
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyArticle',
        ),
        migrations.CreateModel(
            name='Article2',
            fields=[
            ],
            options={
                'verbose_name': '文章复核',
                'verbose_name_plural': '文章复核列表',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('front.article',),
        ),
    ]
