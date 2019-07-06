from django.contrib import admin
from .models import Post

#admin.site.register(Post) #admin에 Post 모델을 등록한다.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['updated_at']
    search_fields = ['title']




