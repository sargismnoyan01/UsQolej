from django.contrib import admin
from .models import *



admin.site.register(AboutCollege)
admin.site.register(Professions)
admin.site.register(ProfDetail)
admin.site.register(ContactUs)
admin.site.register(Dimord)
admin.site.register(PDFiles)
admin.site.register(MyVideo)
admin.site.register(Contact)
admin.site.register(SubStuffs)

@admin.register(Staffs)
class StaffsModelAdmin(admin.ModelAdmin):
    list_display=['name','prof']
    list_display_links=['name','prof']
    search_fields=['name','prof']

@admin.register(Questions)
class QuestionsModelAdmin(admin.ModelAdmin):
    list_display=['question','answer']
    list_display_links=['question','answer']
    search_fields=['question','answer']
