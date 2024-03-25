from django.contrib import admin
from apps.base.models import *
class BannerFilter(admin.ModelAdmin):
    list_display = ("title",)
    list_filter = ("title",)
    search_fields = ("title",)
    readonly_fields = ("description",)

# Register your models here.
admin.site.register(About)
admin.site.register(Command)
admin.site.register(Uslugi, BannerFilter)
admin.site.register(Contact)
admin.site.register(Gallery)
admin.site.register(News)
admin.site.register(Commands)
admin.site.register(Post)
admin.site.register(Banner, BannerFilter)
admin.site.register(Facilties)
admin.site.register(Services)


