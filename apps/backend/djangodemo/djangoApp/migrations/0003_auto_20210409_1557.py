# Generated by Django 3.1.7 on 2021-04-09 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoApp', '0002_auto_20210404_0918'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumberModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('num_orders', models.PositiveSmallIntegerField(default=0)),
                ('num_stocs', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
