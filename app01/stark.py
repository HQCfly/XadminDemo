from stark.service.stark import starkSite,ModelStark

from django.urls import reverse
from .models import *
from app02.models import *

from django.utils.safestring import mark_safe
class UserConfig(ModelStark):


    def edit(self,obj):
        module_name = self.model._meta.model_name
        app_label = self.model._meta.app_label
        #反向解析
        _url = reverse("%s_%s_change"%(app_label,module_name),args=(obj.pk,))
        print("_url:",_url)

        return mark_safe("<a href='%s'>编辑</a>"%_url)



    def delete(self, obj):
        module_name = self.model._meta.model_name
        app_label = self.model._meta.app_label
        # 反向解析
        _url = reverse("%s_%s_delete" % (app_label, module_name), args=(obj.pk,))
        print("_url:", _url)

        return mark_safe("<a href='%s'>删除</a>" % _url)



    def checkbox(self, obj=None, header=False):
        if header:
            return mark_safe('<input id="choice" type="checkbox">')

        return mark_safe('<input class="choice_item" type="checkbox">')



    list_display = [checkbox,"pk","name","age",edit,delete]
starkSite.register(UserInfo,UserConfig)








