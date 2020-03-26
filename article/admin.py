from django.contrib import admin
from article.models import Text, Favorite
# Register your models here.
class TextAdmin(admin.ModelAdmin):

    list_display = ("id","title", "image","uploadtime","text","url", "enable")


class FavoriteAdmin(admin.ModelAdmin):

	list_display = ('user', 'text')


admin.site.register(Text, TextAdmin)
admin.site.register(Favorite, FavoriteAdmin)