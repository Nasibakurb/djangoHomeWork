# Generated by Django 4.2.1 on 2023-06-02 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_alter_mymodel_mymodel2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='myModel3',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='myModel4',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='myModel5',
            field=models.TextField(default=None, null=True),
        ),
    ]
