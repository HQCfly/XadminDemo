from django.contrib import admin

# Register your models here.


from Xadmin.service.Xadmin import site,ModelXadmin
from app02.models import *

from app01.models import *
from django.utils.safestring import  mark_safe

class BookConfig(ModelXadmin):
    def edit(self,obj=None,is_header=False):
        if is_header:
            return "操作"
        # 反向解析：url
        return mark_safe("<a href='%s/change/'>编辑</a>"%obj.pk)

    def delete(self,obj=None,is_header=False):

        if is_header:
            return "操作"

        return mark_safe("<a href=''>删除</a>")

    def check(self,obj=None,is_header=False):
        if is_header:
            return "选择"

        return mark_safe("<input type='checkbox'>")


    list_display=[check,"nid","title","publish",edit,delete]
    #list_display=["nid","title","publish"]

site.register(Book,BookConfig)



site.register(Publish)
site.register(Author)
site.register(AuthorDetail)


