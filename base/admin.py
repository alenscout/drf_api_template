from django.contrib import admin
from .models import ModelOneForTest, ModelTwoForTest

admin.site.register(ModelOneForTest)
admin.site.register(ModelTwoForTest)
