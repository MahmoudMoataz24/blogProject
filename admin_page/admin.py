from django.contrib import admin
<<<<<<< HEAD
# from blog.models import Comments,Likes,Post,userAdds,reply,Category
=======
from blog.models import Comments,Likes,Post,User,reply,Category
>>>>>>> be86348346c474582e9ad09972b5796ebac278da
# Register your models here.

# class PostAdmin(admin.ModelAdmin):
#     list_display=('title','slug','created')
#     list_filter=('title',)
#     search_fields=('title','tag_name')

<<<<<<< HEAD
# admin.site.register(Post,PostAdmin)
=======
admin.site.register(Post,PostAdmin)
>>>>>>> be86348346c474582e9ad09972b5796ebac278da
