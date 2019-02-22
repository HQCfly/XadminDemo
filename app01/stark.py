from django.forms import ModelForm

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
            "price":"价格"
        }
class BookConfig(ModelStark):
    list_display = ["title","price",]
    list_display_links = ["title"]
    modelform_class = BookModelForm

class UserConfig(ModelStark):

    list_display = ["name","age",]
    list_display_links = ["name"]
starkSite.register(UserInfo,UserConfig)

starkSite.register(Book, BookConfig)
starkSite.register(Publish)
starkSite.register(Author)
starkSite.register(AuthorDetail)







