# Generated by Django 3.0 on 2023-06-08 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommodityInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('sezes', models.CharField(max_length=100)),
                ('types', models.CharField(max_length=100)),
                ('price', models.FloatField(verbose_name='商品价格')),
                ('discount', models.FloatField(verbose_name='折后价格')),
                ('stock', models.IntegerField(verbose_name='存货数量')),
                ('sold', models.IntegerField(verbose_name='已售数量')),
                ('likes', models.IntegerField(verbose_name='收藏数量')),
                ('created', models.DateField(auto_now_add=True, verbose_name='上架日期')),
                ('img', models.FileField(upload_to='imgs', verbose_name='商品主图')),
                ('detail', models.FileField(upload_to='detail', verbose_name='商品介绍')),
            ],
            options={
                'verbose_name': '商品信息',
                'verbose_name_plural': '商品信息',
            },
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firsts', models.CharField(max_length=100, verbose_name='一级类型')),
                ('seconds', models.CharField(max_length=100, verbose_name='二级类型')),
            ],
            options={
                'verbose_name': '商品类型',
                'verbose_name_plural': '商品类型',
            },
        ),
    ]
