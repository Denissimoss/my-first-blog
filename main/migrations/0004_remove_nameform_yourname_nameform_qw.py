# Generated by Django 4.0 on 2022-03-06 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_nameform_delete_orm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nameform',
            name='Yourname',
        ),
        migrations.AddField(
            model_name='nameform',
            name='qw',
            field=models.CharField(default=1, max_length=100, verbose_name='name'),
            preserve_default=False,
        ),
    ]
