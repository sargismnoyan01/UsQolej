from django.contrib import admin
from .models import *


admin.site.register(EnAboutCollege)
admin.site.register(EnProfessions)
admin.site.register(EnProfDetail)
admin.site.register(EnDimord)
admin.site.register(EnContactUs)
admin.site.register(EnPDFiles)
admin.site.register(EnMyVideo)
admin.site.register(EnContact)
admin.site.register(EnSubStuffs)


@admin.register(EnStaffs)
class StaffsModelAdmin(admin.ModelAdmin):
    list_display=['name','prof']
    list_display_links=['name','prof']
    search_fields=['name','prof']

@admin.register(EnQuestions)
class QuestionsModelAdmin(admin.ModelAdmin):
    list_display=['question','answer']
    list_display_links=['question','answer']
    search_fields=['question','answer']