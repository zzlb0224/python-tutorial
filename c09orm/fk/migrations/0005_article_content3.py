# Generated by Django 2.2.7 on 2019-12-06 13:03

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fk', '0004_remove_article_content2'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content3',
            field=froala_editor.fields.FroalaField(blank=True),
        ),
    ]
