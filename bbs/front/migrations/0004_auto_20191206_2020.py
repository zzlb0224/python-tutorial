# Generated by Django 2.2.7 on 2019-12-06 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0003_auto_20191206_1707'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '文章', 'verbose_name_plural': '文章列表'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '分类', 'verbose_name_plural': '分类列表'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '评论', 'verbose_name_plural': '评论列表'},
        ),
    ]
