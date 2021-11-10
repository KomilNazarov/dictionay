from django.contrib import admin
from .models import *
import xlsxwriter
from import_export import resources
from import_export.fields import Field


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}


class WordAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("title",)}


class RotatsiyaResource(resources.ModelResource):
    rotation = Field()
    class Meta:
        model = Rotatsiya
        fields = ('id', "word", "user", '_type',)
        export_order = ('id', "word", "user", '_type')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Word, WordAdmin)
admin.site.register(Rotatsiya)
