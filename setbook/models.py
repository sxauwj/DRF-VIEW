from django.db import models


# Create your models here.

# 定义图书、英雄模型类，关系为一对多
class BookInfo(models.Model):
    # verbose_name字段的显示名称
    btitle = models.CharField(max_length=10,verbose_name='书名')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    #  新增属性，上传图片使用
    image = models.ImageField(upload_to='bookset',verbose_name='图片',null=True)
    class Meta:
        # 默认表名称为：应用名称_类名称小写
        # 可以使用如下代码设置名称
        db_table = 'tb_books'
        # 更改模型类的提示文本
        verbose_name = '图书'
        verbose_name_plural = verbose_name
    # 将BOOK对象以字符串的形式显示
    def __str__(self):
        return self.btitle

    # 在Admin的列表中使用这个属性，要求返回字符串
    def pub_date(self):
        # 将日期对象haunt转成字符串 formate
        return self.bpub_date.strftime('%Y-%m-%d')
    pub_date.short_description = '发布日'
    # 方法列不能排序，如果需要排序需要未方法指定排序依据
    pub_date.admin_order_field = 'bpub_date'

class HeroInfo(models.Model):
    GENDER_CHOICES = (
        (0,'女'),
        (1,'男')
    )
    hname = models.CharField(max_length=20)
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES,default=0)
    hcomment = models.CharField(max_length=200,null=True)
    hbook = models.ForeignKey(BookInfo, related_name='heros')
    is_delete = models.BooleanField(default=False)
    class Meta:
        db_table = 'tb_heros'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.hname
    # 访问关联对象成员
    def read(self):
        return self.hbook.bread

    read.short_description = '图书阅读量'



