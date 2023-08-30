from django.contrib import admin

from news_app.models import News,Category,Contact

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','slug','status','category']
    list_filter = ['publish_time','create_time','upload_time','status']
    prepopulated_fields = {'slug':('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['title','body']
    ordering = ['publish_time','status']
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','message']