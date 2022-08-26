# Generated by Django 4.1 on 2022-08-23 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRMapp', '0002_remove_category_name_category_contacted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='contacted',
        ),
        migrations.RemoveField(
            model_name='category',
            name='converted',
        ),
        migrations.RemoveField(
            model_name='category',
            name='new',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lead',
            name='category',
            field=models.ForeignKey(blank=True, default='new', null=True, on_delete=django.db.models.deletion.SET_NULL, to='CRMapp.category'),
        ),
    ]
