# Generated by Django 5.0.6 on 2024-05-27 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('product', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('Delivery_Date', models.DateField()),
            ],
        ),
    ]
