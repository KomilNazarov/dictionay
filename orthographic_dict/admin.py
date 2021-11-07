from django.contrib import admin
from.models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}


class WordAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Word, WordAdmin)
