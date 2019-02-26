from django.forms import ModelForm
from django.http import HttpResponse

from stark.service.stark import starkSite,ModelStark

from django.urls import reverse
from .models import *
from app02.models import *

from django.utils.safestring import mark_safe
class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

        labels={
            "title":"书籍名称",
            "price":"价格",
            "publish": "出版社",
            "authors": "作者",
        }
class BookConfig(ModelStark):
    list_display = ["title","price","publish","authors"]
    list_display_links = ["title"]
    search_fields = ["title", "price"]
    modelform_class = BookModelForm

    def patch_init(self, request, queryset):
        queryset.update(price=123)

        return HttpResponse("批量初始化OK")

    patch_init.short_description = "批量初始化"

    actions = [patch_init]
    list_filter = ["title", "publish", "authors", ]


class UserConfig(ModelStark):

    list_display = ["name","age",]
    list_display_links = ["name"]
    search_fields = ["name", "age"]
starkSite.register(UserInfo,UserConfig)

starkSite.register(Book, BookConfig)
starkSite.register(Publish)
starkSite.register(Author)
starkSite.register(AuthorDetail)







