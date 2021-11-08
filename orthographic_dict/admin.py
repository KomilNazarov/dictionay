from django.contrib import admin
from .models import *
import xlsxwriter


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}


class WordAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("title",)}
    list_filter = ['word__title']

class RotatsiyaAdmin(admin.ModelAdmin):
    def exel(self, request, queryset):
        if request.user.is_superuseer:
            # create file(workbook) and worksheet
            outWorkbook = xlsxwriter.Workbook("hisobot.xlsx")
            outSheet = outWorkbook.add_worksheet()

            # write headers
            outSheet.write("A1", "Username")
            outSheet.write("B1", "Bilaman")
            outSheet.write("C1", "Bilmayman")



admin.site.register(Category, CategoryAdmin)
admin.site.register(Word, WordAdmin)
