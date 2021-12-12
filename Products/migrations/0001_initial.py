# Generated by Django 4.0 on 2021-12-12 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=64)),
                ('product_location', models.CharField(max_length=256)),
                ('product_description', models.TextField(blank=True, default='', null=True)),
                ('product_price', models.IntegerField(default=0)),
                ('product_img_1', models.CharField(max_length=256)),
                ('product_img_2', models.CharField(max_length=256)),
                ('product_img_3', models.CharField(max_length=256)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.category')),
                ('product_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.newuser')),
            ],
        ),
    ]
