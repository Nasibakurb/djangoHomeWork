# Generated by Django 4.2.1 on 2023-06-02 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myModel1', models.CharField(default=None, max_length=10)),
                ('myModel2', models.CharField(default=None, max_length=20)),
                ('myModel3', models.CharField(default=None, max_length=50)),
                ('myModel4', models.TextField(default=None)),
                ('myModel5', models.TextField(default=None)),
            ],
        ),
    ]
