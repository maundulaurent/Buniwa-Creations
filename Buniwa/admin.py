from django.contrib import admin
from .models import *


class theFaqsAdmin(admin.ModelAdmin):
    list_display = ('question',)

admin.site.register(PortfolioPost)
admin.site.register(theTeam)
admin.site.register(theFaqs, theFaqsAdmin)
admin.site.register(theTestimonials)
admin.site.register(theServices)
admin.site.register(blogComment)
admin.site.register(TextEntry)
admin.site.register(theCompany)

@admin.register(theBlog)
class theBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'published_date')
    search_fields = ('title', 'content')
    list_filter = ('category', 'author')
    date_hierarchy = 'published_date'

# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'author', 'published_date')
#     search_fields = ('title', 'content')
#     list_filter = ('category', 'author')
#     date_hierarchy = 'published_date'
