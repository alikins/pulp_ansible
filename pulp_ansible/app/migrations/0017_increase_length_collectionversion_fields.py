# Generated by Django 2.2.12 on 2020-05-14 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ansible', '0016_add_extension'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionversion',
            name='documentation',
            field=models.URLField(blank=True, default='', editable=False, max_length=2000),
        ),
        migrations.AlterField(
            model_name='collectionversion',
            name='homepage',
            field=models.URLField(blank=True, default='', editable=False, max_length=2000),
        ),
        migrations.AlterField(
            model_name='collectionversion',
            name='issues',
            field=models.URLField(blank=True, default='', editable=False, max_length=2000),
        ),
        migrations.AlterField(
            model_name='collectionversion',
            name='repository',
            field=models.URLField(blank=True, default='', editable=False, max_length=2000),
        ),
    ]