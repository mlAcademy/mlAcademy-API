# Generated by Django 2.1.4 on 2019-02-18 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0006_auto_20190218_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='lesson1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lesson1', to='lessons.Lesson'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='lesson10',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lesson10', to='lessons.Lesson'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='lesson2',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lesson2', to='lessons.Lesson'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='lesson3',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lesson3', to='lessons.Lesson'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='lesson4',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lesson4', to='lessons.Lesson'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='lesson5',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lesson5', to='lessons.Lesson'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='lesson6',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lesson6', to='lessons.Lesson'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='lesson7',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lesson7', to='lessons.Lesson'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='lesson8',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lesson8', to='lessons.Lesson'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='lesson9',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lesson9', to='lessons.Lesson'),
        ),
    ]