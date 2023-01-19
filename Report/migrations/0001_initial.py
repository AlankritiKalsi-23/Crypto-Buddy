# Generated by Django 4.0.3 on 2022-09-19 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='listOfCoins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coinName', models.CharField(max_length=150)),
                ('priceUSD', models.DecimalField(decimal_places=20, max_digits=25)),
            ],
        ),
    ]