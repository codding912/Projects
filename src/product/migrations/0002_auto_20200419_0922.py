# Generated by Django 3.0.5 on 2020-04-19 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]