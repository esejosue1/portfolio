from django.contrib import admin
from .models import Projects, Category, Knowledge, Experience

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')
    

class KnowledgeAdmin(admin.ModelAdmin):
    list_display=("title", "slug", "category", "level")
    prepopulated_fields = {'slug': ('title',)}
    

class ExperienceAdmin(admin.ModelAdmin):
    list_display=("title", "company", "start_date","end_date","current")

# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Projects)
admin.site.register(Knowledge, KnowledgeAdmin)
admin.site.register(Experience,ExperienceAdmin)
