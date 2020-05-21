from django.contrib import admin
from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    '''
    list_display:后台的文章列表显示中显示的内容
    fiedls:控制表单创建与修改页显示的字段,创建时间，修改时间，还有作者是没必要展示的
    '''
    list_display = ['title','views','created_time','modified_time','category','author']
    fields = ['title','body','excerpt','category','tags']

    def save_model(self, request, obj, form, change):
        '''
        用于将创建的帖子的作者改为后台登录的用户
        :param obj: 包含着创建帖子各个字段，包括author
        '''
        obj.author = request.user
        super().save_model(request,obj,form,change)

#Post和PostAdmin应该注册在一起
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)