from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','url','post','created_time'] #用于列表页的展示的字段
    fields = ['name','email','url','text','post'] #用于创建和修改详情页显示的字段

admin.site.register(Comment,CommentAdmin)
