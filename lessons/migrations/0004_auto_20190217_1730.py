# Generated by Django 2.1.5 on 2019-02-17 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='description',
            field=models.TextField(default='lesson description'),
        ),
        migrations.AddField(
            model_name='topic',
            name='prerequisites',
            field=models.ManyToManyField(blank=True, related_name='prerequisites_rname', related_query_name='prerequisites_rqueryname', to='lessons.Topic'),
        ),
    ]
