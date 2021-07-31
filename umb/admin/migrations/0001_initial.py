# Generated by Django 3.2.5 on 2021-07-17 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=191)),
                ('bruto', models.FloatField()),
                ('tara', models.FloatField()),
                ('netto', models.FloatField()),
                ('discount', models.FloatField()),
                ('amount_weight', models.FloatField()),
                ('price', models.FloatField()),
                ('price_price', models.FloatField()),
                ('paid_off', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Weight',
                'verbose_name_plural': 'Weights',
            },
        ),
    ]