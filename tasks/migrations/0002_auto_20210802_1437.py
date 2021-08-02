# Generated by Django 3.2.5 on 2021-08-02 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('created',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['created']},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
