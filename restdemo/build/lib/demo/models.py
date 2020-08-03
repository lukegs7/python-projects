from django.db import models


class UserEntity(models.Model):
    name = models.CharField(max_length=20, verbose_name='用户名')

    class Meta:
        db_table = 't_user'
        verbose_name = '用户表'
        verbose_name_plural = '用户表'

class Contact(models.Model):
    # 联系方式
    address = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    user = models.OneToOneField(UserEntity, on_delete=models.CASCADE,related_name='contact')

    class Meta:
        db_table = 'contact'
        verbose_name = verbose_name_plural = '联系人'


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'category'
        verbose_name = verbose_name_plural = '类别'


class FruitEntity(models.Model):
    name = models.CharField(max_length=20, verbose_name='水果名')
    price = models.FloatField(verbose_name='价格')
    source = models.CharField(max_length=30, verbose_name='源产地')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='fruits')
    # 默认反向引用的名称是类名(小写)_set
    users = models.ManyToManyField(UserEntity, db_table='t_collect', related_name='fruits', verbose_name='收藏用户列表')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_fruit'
        verbose_name = '水果表'
        verbose_name_plural = verbose_name
