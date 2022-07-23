from django.contrib import admin

# Register your models here.

from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

app_models = apps.get_app_config("img_db").get_models()  # 获取app:crm下所有的model,得到一个生成器
# 遍历注册model
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass