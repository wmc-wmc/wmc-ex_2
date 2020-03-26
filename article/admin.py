from django.contrib import admin
from article.models import Text
# Register your models here.
class TextAdmin(admin.ModelAdmin):
    list_display = ("id","title", "image","uploadtime","text","source")
admin.site.register(Text, TextAdmin)