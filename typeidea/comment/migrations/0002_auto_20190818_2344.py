# Generated by Django 2.2.3 on 2019-08-18 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Post', verbose_name='评论目标'),
        ),
    ]
