from django.db import models


# Create your models here.

class Types(models.Model):
    id = models.AutoField(primary_key=True)
    firsts = models.CharField('一级类型', max_length=100)
    seconds = models.CharField('二级类型', max_length=100)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '商品类型'
        verbose_name_plural = '商品类型'


class CommodityInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sezes = models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    price = models.FloatField('商品价格')
    discount = models.FloatField('折后价格')
    stock = models.IntegerField('存货数量')
    sold = models.IntegerField('已售数量')
    likes = models.IntegerField('收藏数量')
    created = models.DateField('上架日期', auto_now_add=True)
    img = models.FileField('商品主图', upload_to=r'imgs')
    detail = models.FileField('商品介绍', upload_to=r'detail')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = '商品信息'
