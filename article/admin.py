from django.contrib import admin
from article.models import Text, Favorite, Tag, Comment
# Register your models here.
class TextAdmin(admin.ModelAdmin):

    list_display = ("id","title", "image","uploadtime","text","url", "enable")


class FavoriteAdmin(admin.ModelAdmin):

	list_display = ('user', 'text')


class TagAdmin(admin.ModelAdmin):

	list_display = ('name', )

class TypeAdmin(admin.ModelAdmin):

	list_display = ('name', )

class CommentAdmin(admin.ModelAdmin):

	list_display = ('user', 'text', 'content')


admin.site.register(Text, TextAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Type, TypeAdmin)