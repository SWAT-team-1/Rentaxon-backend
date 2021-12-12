# Generated by Django 4.0 on 2021-12-12 15:04

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
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_content', models.CharField(max_length=256)),
                ('auther', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auther', to='accounts.newuser')),
                ('reviewed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewed', to='accounts.newuser')),
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
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_favorite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.newuser')),
            ],
        ),
    ]
