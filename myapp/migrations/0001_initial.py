# Generated by Django 3.2.4 on 2022-12-03 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bird',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_Main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]