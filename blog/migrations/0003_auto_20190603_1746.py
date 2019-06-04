# Generated by Django 2.2.1 on 2019-06-04 00:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete='models.PROTECTED', related_name='comments', to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete='models.PROTECTED', related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
