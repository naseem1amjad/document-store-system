# Generated by Django 4.0.2 on 2022-02-14 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0007_document_topics_alter_topic_topic_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='topics',
            field=models.ManyToManyField(related_name='documents', to='myapi.Topic'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='topics',
            field=models.ManyToManyField(related_name='folders', to='myapi.Topic'),
        ),
    ]
