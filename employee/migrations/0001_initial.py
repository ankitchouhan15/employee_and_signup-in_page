# Generated by Django 4.1.3 on 2022-12-28 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="employee",
            fields=[
                ("eid", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("age", models.IntegerField()),
                ("mobile", models.CharField(max_length=12, unique=True)),
                ("email", models.EmailField(max_length=25, unique=True)),
                ("city", models.CharField(max_length=25)),
                ("salary", models.FloatField()),
            ],
        ),
    ]
