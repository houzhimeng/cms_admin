from django.db import models

# Create your models here.

class UserInfo(models.Model):
    #自动创建id，主键
    #用户名，列 字符串类型，指定长度
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64,error_messages={'required': '请输入密码'})
    email = models.CharField(max_length=60)
    test = models.CharField(max_length=19,null=True)
    user_group = models.ForeignKey("UserGroup",to_field='uid')
    user_type_choices = (
        (1,'超级用户'),
        (2,'普通用户'),
        (3,'一般用户'),
    )

    user_type_id = models.IntegerField(choices=user_type_choices,default=1)


class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32)
    ctime = models.DateField(auto_now_add=True, null=True)
    uptime = models.DateField(auto_now_add=True, null=True)

