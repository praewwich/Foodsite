from FoodApp.models import Post,Category,Subscribe
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','user','Category','title','list_date','image','is_public')
    list_display_links = ('id','title')
    search_fields = ('id','title',)
 
    def Postimage(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
            )
    )
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email',)

admin.site.register(Post,PostAdmin)
admin.site.register(Subscribe,SubscribeAdmin)
admin.site.register(Category,CategoryAdmin)


