from django.contrib import admin
from .models import Post, Category, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)} # new


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)