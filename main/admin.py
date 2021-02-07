from django.contrib import admin
from solo.admin import SingletonModelAdmin
from . models import SiteConfig
from . models import Blog
from . models import Comments
from . models import Partners
from . models import Services
from . models import Portfolio

def make_published(modeladmin, request, queryset):
    queryset.update(status='public')

make_published.short_description = "Опубликовать выбранные"

class AdminComments(admin.ModelAdmin):
    list_display = ['author', 'status']
    ordering = ['author']
    actions = [make_published]

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.site_header = 'DIAMANT'
admin.site.register(Blog, PostAdmin)
admin.site.register(Comments, AdminComments)
admin.site.register(Partners)
admin.site.register(Services)
admin.site.register(Portfolio)
admin.site.register(SiteConfig, SingletonModelAdmin)