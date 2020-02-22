from django.contrib import admin
from blog.models import Comments,Likes,Post,User,reply,Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','created')
    list_filter=('title',)
    search_fields=('title','tag_name')

admin.site.register(Post,PostAdmin)
