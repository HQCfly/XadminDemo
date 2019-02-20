#Django的Xadmin流程以及原理
url()的使用

    情况1：url(r'^book/', views.book),  # book(request)

    情况2 分发：
    url(r"^twiss/", ([
                       url(r'^test01/', ([
                                             url(r'^test04/', test04),
                                             url(r'^test05/', test05),
                                         ], None, None)),
                       url(r'^test02/', test02),
                       url(r'^test03/', test03),
                   ], None, None)
       )

    单例模式
       生成单例模式的方式：
       （1）使用 __new__
       （2）使用模块
            class A()
               pass
            a=A()

            admin源码:
            1 启动文件
            class StarkConfig(AppConfig):
               name = 'stark'
               def ready(self):
                   autodiscover_modules('stark')

            2 注册 admin.py

                admin.site.register(Book,BookConfig)

                源码：

                    class AdminSite():
                         def __init__(self, name='admin'):
                             self._registry = {}

                         def register(self,model,admin_class):
                             if not admin_class:
                                  admin_class = ModelAdmin

                             self._registry[model] = admin_class(model, self)

                    site=AdminSite()

            3 设计url

                如何通过model类变量获取该模型的字符串名称和该模型所在app的字符串名称：
                print("===>", model._meta.model_name)
                print("===>", model._meta.app_label)

在ModelStark中：
       self.model: 用户当前访问的模型表

 查看页面：
      表头
      表数据
      search
      action
      分页
      filter

  增删改（modelForm）

   pop