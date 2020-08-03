from django.db import models

# Create your models here.

class Node(models.Model):
    name=models.TextField(max_length=50,verbose_name='节点名称')
    create_time=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    class Meta:
        db_table='node'


class Module(models.Model):
    name=models.TextField(max_length=50,verbose_name='模块名称')
    nodes=models.ManyToManyField(Node,related_name='module',verbose_name='节点')
    class Meta:
        db_table='module'